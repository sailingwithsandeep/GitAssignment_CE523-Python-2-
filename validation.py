import re


def validation(email,mobile):
    email_pattern = re.findall(r'[A-z0-9]\S+@[A-z-]+[.][A-z]{2,3}',email)
    mobile_pattern = re.findall(r'\d{10,12}',mobile)
    if email_pattern and mobile_pattern:
        return True
    else:
        print('Email or mobile is invalid peace out!\n')