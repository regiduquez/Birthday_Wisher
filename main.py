##################### Extra Hard Starting Project ######################
import pandas as pd
import datetime as dt
import random as rd
import smtplib

MY_EMAIL = 'reginaldduquez@outlook.com'
MY_PASS = '#AbbyRegi4ever'




# 1. Update the birthdays.csv
bday_df = pd.read_csv("birthdays.csv")
bday_list = [{'name':row['name'],'email':row['email'],
              'year':row['year'],'month':row['month'],
              'day':row['day']} for index, row in bday_df.iterrows()]


# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
for i in bday_list:
    if i['month'] == now.month and i['day'] == now.day:
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        with open(f'letter_templates/letter_{rd.randint(1,3)}.txt','r') as let_temp:
            letter_to_send = let_temp.read()
            letter_to_send = letter_to_send.replace('[NAME]', i['name'])
# 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP('smtp-mail.outlook.com', port=587) as smtp:
            smtp.starttls()
            smtp.login(MY_EMAIL, MY_PASS)
            smtp.sendmail(MY_EMAIL,i['email'], msg=f"Subject:Happy Birthday!\n\n{letter_to_send}")





