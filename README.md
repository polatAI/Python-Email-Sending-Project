# Python-Email-Sending-Project
Python Email Sending Project
# 📧 Python E-posta Gönderme Projesi 📧

![Türkçe Klavuz](https://img.shields.io/badge/Dil-T%C3%BCrk%C3%A7e-yellow)
[English Manual](#python-email-sending-project-)

Bu Python projesi, `smtplib` ve MIME (Multipurpose Internet Mail Extensions) türlerini kullanarak e-posta göndermeye olanak sağlar. Projeyi kullanarak belirtilen e-posta hesabından alıcıya metin içeriği ve ek olarak resimli bir e-posta gönderebilirsiniz.

## 🚀 Başlangıç

Bu talimatlar, projeyi yerel makinanızda çalıştırmak ve geliştirmek için size yol gösterecektir. E-posta hesabı ve SMTP sunucusu yapılandırmasını dikkate alarak doğru çalışmasını sağlayın.

### 📋 Gereksinimler

Projenin çalışması için aşağıdaki gereksinimlere ihtiyacınız olacak:

- Python 3.x
- `smtplib` modülü
- `os` modülü

### 🔧 Kurulum

1. Bu depoyu yerel makinenize klonlayın:

git clone https://github.com/KULLANICI_ADINIZ/eposta-gonderme-projesi.git

markdown
Copy code

2. Proje dizinine gidin:

cd eposta-gonderme-projesi

markdown
Copy code

3. Yapılandırma dosyanızı ekleyin:

Projeyi çalıştırmadan önce `config.json` dosyasını düzenleyin ve gerekli e-posta hesabı bilgilerinizi ve e-posta göndermek istediğiniz alıcının adresini girin.

{
"sender_email": "gonderen@ornek.com",
"sender_pwd": "gonderen_sifre",
"recipient_email": "alici@ornek.com"
}

markdown
Copy code

4. Proje dosyasını çalıştırın:

python main.py

yaml
Copy code


---

# 📧 Python Email Sending Project 📧

![English](https://img.shields.io/badge/Language-English-blue)
[Türkçe](#python-e-posta-g%C3%B6nderme-projesi-)

This Python project allows you to send emails using `smtplib` and MIME (Multipurpose Internet Mail Extensions) types. You can send text content along with an attached image from the specified email account to the recipient.

## 🚀 Getting Started

These instructions will guide you to run and develop the project on your local machine. Make sure to configure your email account and SMTP server for proper functioning.

### 📋 Prerequisites

You will need the following prerequisites for the project to work:

- Python 3.x
- `smtplib` module
- `os` module

### 🔧 Installation

1. Clone this repository to your local machine:

git clone https://github.com/YOUR_USERNAME/email-sending-project.git

csharp
Copy code

2. Change into the project directory:

cd email-sending-project

arduino
Copy code

3. Add your configuration file:

Before running the project, edit the `config.json` file and enter your email account credentials and the recipient's email address.

{
"sender_email": "sender@example.com",
"sender_pwd": "sender_password",
"recipient_email": "recipient@example.com"
}

markdown
Copy code

4. Run the project file:

python main.py

yaml
Copy code


---
