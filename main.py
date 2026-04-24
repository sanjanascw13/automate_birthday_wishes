# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


import datetime as dt
import pandas
import smtplib
import os

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

to_replace = "[Name]"
my_mail = "sanjanascw13@gmail.com"
password = "rsoaleceiudchfpp"

#Date
now = dt.datetime.now()
day = now.day
month = now.month

#Email
connection = smtplib.SMTP(host="smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=my_mail, password=password)

#Functions
def checker(dictionary_name):
    birthday_list = []
    for i in dictionary_name:
        check_month = i.get("month")
        check_day = i.get("day")
        if check_month == month and check_day == day:
            birthday_list.append(i)
    return birthday_list


def mail_send(list_name):
    for j in list_name:
        birthday_name = j.get("name")
        birthday_mail = j.get("email")

        with open(file="letter.txt", mode="r", encoding="utf-8") as letter:
            lines = letter.readlines()
            new_line = lines[0].replace(to_replace, birthday_name)
            lines[0] = new_line

        body = ""

        for k in lines:
            body = body + k

        message = f"Subject : Happy Birthday {birthday_name}\n\n{body}"
        connection.sendmail(from_addr=my_mail, to_addrs=birthday_mail, msg=message)


#CSV file
birthdays_data = pandas.read_csv("birthdays.csv")
birth_dict = birthdays_data.to_dict(orient = "records")

birthday_boy = checker(birth_dict)
mail_send(birthday_boy)
connection.close()
