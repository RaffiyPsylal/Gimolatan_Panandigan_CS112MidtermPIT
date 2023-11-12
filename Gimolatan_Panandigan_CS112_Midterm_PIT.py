# import secrets is a python module used for generating strong random numbers suitable for managing data such as passwords, account authentication, and related secrets.
# import string is a  python module used to see ifa character, slice, or string contains letters, digits, symbols, etc.
# import random is a python module that defines a series of functions for generating or manipulating random integers.
import secrets
import string
import random
# import secrets is a python module used for generating strong random numbers suitable for managing data such as passwords, account authentication, and related secrets.
# import string is a  python module used to see ifa character, slice, or string contains letters, digits, symbols, etc.
# import random is a python module that defines a series of functions for generating or manipulating random integers.

# string.ascii_lowercase is a string constant that gives a lowercase letter from a-z
# string.ascii_uppercase is a string constant that gives an uppercase letter from A-Z
# string.digits gives a number from 0-9
# string.punctuation is a constant string that contains all punctuation characters

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
special = string.punctuation
allChars = lower + upper + digits + special
password = ""

#  This is where you input the length of the password, the number of uppercase and lowercase letters, the number of digits the password will have and also the number of special characters in the password
print ("!WELCOME TO THIS RANDOM PASSWORD GENERATOR! ")
print ("")
pwLen = int(input("How long should the password be? "))
minUpper = int(input("Minimum Upper Case: "))
minLower = int(input("Minimum Lower Case: "))
minDigits = int(input("Minimum Numbers: "))
minSpec = int(input("Minimum Special: "))

for i in range(minUpper):
    # This takes in a sequence as an arguement and returns a randomly chosen element
    password += "".join(random.choice(secrets.choice(upper)))

for i in range(minLower):
    # This takes in a sequence as an arguement and returns a randomly chosen element
    password += "".join(random.choice(secrets.choice(lower)))

for i in range(minDigits):
    # This takes in a sequence as an arguement and returns a randomly chosen element
    password += "".join(random.choice(secrets.choice(digits)))

for i in range(minSpec):
    # This takes in a sequence as an arguement and returns a randomly chosen element
    password += "".join(random.choice(secrets.choice(special)))

remaining = pwLen - minLower - minUpper - minDigits - minSpec

for i in range(remaining):
    # This takes in a sequence as an arguement and returns a randomly chosen element
    password += "".join(random.choice(secrets.choice(allChars)))

password = list(password)
random.shuffle(password)
print("".join(password))
