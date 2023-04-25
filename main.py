import pandas as pd
import smtplib
import datetime as dt
import random

my_email = "testpython172000@gmail.com"
password = "ggrwqvecdgtfoxur"
now = dt.datetime.today()
today_day = now.day
today_month = now.month

today_tuple = (today_month, today_day)


data = pd.read_csv('birthdays.csv')

birthdays_dict = {(row.month, row.day): row for (index, row) in data.iterrows()}

if today_tuple in birthdays_dict:
    random_letter = random.randint(1, 3)
    birthday_person = birthdays_dict[today_tuple]
    file_path = f'letter_templates/letter_{random_letter}.txt'
    with open(file_path) as file:
        letter = file.read()
        letter = letter.replace("[NAME]", birthday_person["name"])

    destination = birthday_person["email"]
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=f"{destination}",
            msg=f"subject:Happy Birthday\n\n{letter}"
        )



