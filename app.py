import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Gönderici Bilgileri
sender_email = "gönderici_maili@gmail.com"
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = "gönderici_maili@gmail.com"
smtp_app_password = "gmailden aldığınız uygulama şifresi"

# Mail gövdesini oluşturunuz.
subject = "Mail başlığı"
message = "mail mesajı"

# Alıcı Bilgilerini girin.
recipient_emails = ["alici_maili1@outlook.com.tr", "alici_maili2@gmail.com", "alici_maili3@gmail.com"]

# Maili gönder
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_app_password)

    for recipient_email in recipient_emails:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        server.sendmail(sender_email, recipient_email, msg.as_string())
        print(f"Email sent to {recipient_email}")

    server.quit()
except Exception as e:
    print("An error occurred while sending the email:", str(e))
