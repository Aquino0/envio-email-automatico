# 📧 Envio Automático de E-mails com Anexo e CC

Este projeto é um script em Python para envio de e-mails automáticos com anexo e cópia (CC). 
Ideal para automatizar comunicados e relatórios diários.

## 🛠️ Tecnologias Utilizadas
- Python 3.10+
- smtplib (Envio de e-mails)
- email (Construção do conteúdo do e-mail)
- pandas (Manipulação de dados para anexos)

## 📋 Pré-requisitos
1. **Instalar o Python:** [Download Python](https://www.python.org/downloads/)
2. **Instalar o Git:** [Download Git](https://git-scm.com/downloads)

## 🚀 Como Configurar e Executar
### 1️⃣ Clonar o Repositório
```bash
git clone https://github.com/seuusuario/envio-email-automatico.git
cd envio-email-automatico
```

### 2️⃣ Criar Ambiente Virtual (Opcional, Recomendado)
```bash
python -m venv venv
source venv/bin/activate  # Para Mac/Linux
venv\Scripts\activate   # Para Windows
```

### 3️⃣ Instalar Dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Configurar Variáveis de Ambiente
Crie um arquivo `.env` com seu e-mail e senha:
```env
EMAIL_REMETENTE="seuemail@example.com"
SENHA="suasenha"
```

### 5️⃣ Executar o Script
```bash
python enviar_email.py
```

## 📝 Arquivos Importantes
- `enviar_email.py`: Script principal de envio.
- `requirements.txt`: Bibliotecas necessárias.
- `.env`: Configuração de credenciais.
- `README.md`: Documentação completa.

## 📚 Instalar Bibliotecas Manualmente (Se necessário)
```bash
pip install pandas smtplib email python-dotenv
```

## Contato - [text](https://www.linkedin.com/in/cristopher-aquino-4992b251/)
