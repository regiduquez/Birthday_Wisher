from email.message import EmailMessage
import smtplib
import datetime as dt
import random as rd

DAYS_OF_WEEK = ["Monday","Tuesday","Wednesday","Thursday", "Friday", "Saturday", "Sunday"]

with open("quotes.txt", 'r') as quotes:
    quotes_list = quotes.readlines()
quotes_day = rd.choice(quotes_list)
print(quotes_day)

now = dt.datetime.now()
this_day = now.weekday()


def send_mail():
    my_email = "reginaldduquez@outlook.com"
    my_password = "#AbbyRegi4ever"
    recipient_email = "reginaldduquez@yahoo.com"

    subject = f"Happy {DAYS_OF_WEEK[this_day]} this is your quote of the day!"
    body = quotes_day

    em = EmailMessage()
    em['From'] = my_email
    em['To'] = recipient_email
    em['Subject'] = subject
    em.set_content(body)

    with smtplib.SMTP("smtp-mail.outlook.com", port=587) as smtp:
        smtp.starttls()
        smtp.login(my_email, my_password)
        smtp.sendmail(my_email, recipient_email, em.as_string())

if now.weekday() == DAYS_OF_WEEK.index("Wednesday"):
    send_mail()







