import pandas as pd
import win32com.client as win32
import os

# Carrega o arquivo Excel
df = pd.read_excel(r"Z:\C - Relatórios\Parametros_Email_Automatico.xlsx")

# Inicializa o Outlook
outlook = win32.Dispatch('Outlook.Application')
namespace = outlook.GetNamespace('MAPI')

# Percorre cada linha do DataFrame para enviar o e-mail
for i, contato in enumerate(df['EMAIL']):
    email = outlook.CreateItem(0)  # Cria um novo item de e-mail
    email.Subject = df['assunto'][i]  # Assunto do e-mail
    email.Body = '''Boa tarde,

Segue parcial do Orçado x Realizado - 2025.

Favor verificar os lançamentos e caso haja dúvida ou necessidade de correção estaremos à disposição. 

Atenciosamente,
'''  # Corpo do e-mail
    email.To = contato  # Destinatário

    # Adiciona alguém em cópia (CC) se existir
    cc = None  # Inicializa a variável
    if 'CC' in df.columns and pd.notna(df['CC'][i]):
        cc = df['CC'][i]
        email.CC = cc

    # Verifica se há um anexo e se o arquivo existe
    if pd.notna(df['ANEXO'][i]):
        arquivo = df['ANEXO'][i].strip()  # Remove espaços extras ao redor do caminho do arquivo
        if os.path.exists(arquivo):
            email.Attachments.Add(arquivo)  # Adiciona o anexo
        else:
            print(f"Erro: O arquivo '{arquivo}' não foi encontrado.")
    
    # Envia o e-mail
    email.Send()

    # Exibe o log
    print(f"E-mail enviado para: {contato} com cópia para: {cc if cc else 'Nenhum'}")