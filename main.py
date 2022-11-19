# Generate random strong password.

import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "!@€#£$%^&*()_-=+"

use_for_password = lower_case + upper_case + number + symbols
password_length = 24

count = 10000000
while count != 0:
    password = "".join(random.sample(use_for_password, password_length))
    print("Your secure password is: ", password)
    count -= 1
