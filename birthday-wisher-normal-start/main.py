
import datetime as dt
import pandas
import smtplib
import random

My_EMAIL = "krishnendumisra68@gmail.com"
PASSWORD="wkdanjgekccirqbg"

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Create a tuple from today's month and day using datetime. e.g.
# today = (today_month, today_day)
today_tuple=(dt.datetime.now().month,dt.datetime.now().day)
# HINT 2: Use pandas to read the birthdays.csv
data=pandas.read_csv('birthdays.csv')
# HINT 3: Use dictionary comprehension to create a dictionary from birthday.csv that is formated like this:
# birthdays_dict = {
#     (birthday_month, birthday_day): data_row
# }
#Dictionary comprehension template for pandas DataFrame looks like this:
# new_dict = {new_key: new_value for (index, data_row) in data.iterrows()}
birthday_dict={(data_row.month,data_row.day): data_row for (index, data_row) in data.iterrows()}
#e.g. if the birthdays.csv looked like this:
# name,email,year,month,day
# Angela,angela@email.com,1995,12,24
#Then the birthdays_dict should look like this:
# birthdays_dict = {
#     (12, 24): Angela,angela@email.com,1995,12,24
# }

 # Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:
if today_tuple in birthday_dict:
    filepath=f"letter_templates/letter_{random.randint(1,3)}.txt"
    birthday_person=birthday_dict[today_tuple]
    with open(filepath) as letter_file:
        contents=letter_file.read()
        contents=contents.replace("[NAME]",birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(My_EMAIL,PASSWORD)
        connection.sendmail(from_addr=My_EMAIL,to_addrs=birthday_person["email"],msg=f"Subject:Happy birthday!"
                                                                                     f"\n\n{contents}")






