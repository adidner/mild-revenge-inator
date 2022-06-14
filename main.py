
from vars import first_name, last_name, email, phone_number


gather_data = input("Hit enter to use the data in vars.py, otherwise enter the first name of the target: ")
if gather_data != "":
    first_name = gather_data
    last_name = input("enter targets last_name")
    email = input("enter targets email")
    phone_number = input("enter targets phone number (with no dashes or parentheses)")


print(first_name)
print(last_name)
print(email)
print(phone_number)


    