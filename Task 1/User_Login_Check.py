# Predefined credentials
username = "admin"
password = "1234"


# User input
input_username = input("Enter username: ")
input_password = input("Enter password: ")


# Authentication check
if input_username == username and input_password == password:
    print("Login Successful")
else:
    print("Invalid Credentials")

    