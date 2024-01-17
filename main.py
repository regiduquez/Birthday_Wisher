from email.message import EmailMessage
import smtplib
import datetime as dt
import random as rd

DAYS_OF_WEEK = ["Monday","Tuesday","Wednesday","Thursday", "Friday", "Saturday", "Sunday"]
now = dt.datetime.now()

with open("quotes.txt") as quotes:
    quotes_list = quotes.readlines()
    quotes_day = rd.choice(quotes_list)

def send_mail():
    my_email = "reginaldduquez@outlook.com"
    my_password = "#AbbyRegi4ever"
    recipient_email = "reginaldduquez@yahoo.com"

    subject = f"Happy {DAYS_OF_WEEK[now.weekday()]} this is your quote of the day!"
    body = quotes_day

    with smtplib.SMTP("smtp-mail.outlook.com", port=587) as smtp:
        smtp.starttls()
        smtp.login(my_email, my_password)
        smtp.sendmail(my_email, recipient_email, msg=f"Subject:{subject}\n\n{body}")



if now.weekday() == DAYS_OF_WEEK.index("Wednesday"):
    send_mail()







