import random
import string
from pprint import pprint

# Accept User Data --- Suggest pw ,If suggested random PW is picked , Store
# If suggested random is not picked , allow pick and verify, then store
# Store User Data --- Store accepted user data
# Display the data
# Start the code

employee_data = []
random_char = string.ascii_lowercase + string.ascii_uppercase + string.digits


def accept_user_data():
    first_name = input("What is your first name?\n ")
    last_name = input("What is your last name?\n ")
    full_name = first_name + " " + last_name
    email = input("What is your email address?\n ")
    random_length = 5
    random_text = ''.join(random.choice(random_char) for i in range(random_length))
    password = first_name[:2] + random_text + last_name[-2:]
    print("Do you accept the computer generated password :", password, "?")
    response = ""
    response = input("Type Y(es) or N(o)")
    if response == "Y":
        store_user_data(full_name, email, password)
    else:
        user_password = picked_password_verification()
        store_user_data(full_name, email, user_password)


def picked_password_verification():
    user_password = input("What password would you like? - ")
    while len(user_password) < 7 :
        print("Password should be equal or greater than 7 ")
        user_password = input("Enter a different password - ")
    else:
        print("Your preferred password is {}" .format(user_password))
        return user_password


def store_user_data(full_name, email, password):
    # Empty list with user details
    user_info = {"Full name ": full_name, "Email": email, "Password": password}
    employee_data.append(user_info)
    display_user_data()


def display_user_data():
    # Loop to check if users want to add more data before it is displayed
    terminate = input("Data Entry Complete ?  Y or N - ").upper()
    if terminate == 'Y':
        print("------USERS------")
        pprint(employee_data)
    else:
        accept_user_data()


accept_user_data()
