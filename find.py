import pyperclip
import re

# copies
# Call me at 512-233-1233 tomorrow. 401-421-4214 is my office.
# Find me at aSd@das.net tomorrow. Also 32k32@asd7a.com is my office.
# Call me at 512-233-1233 tomorrow. Also fasFs@ds3d.att is my office.

text = pyperclip.paste()
print(text)
print()

# lookForPhone = re.compile(r"\d{3}-\d{3}-\d{4}")
lookForPhone = re.compile(r'''(
    (\d{3}|\(\d{3}\))?
    (\s|-|\.)?
    (\d{3})
    (\s|-|\.)
    (\d{4})
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  #extension
)''',re.VERBOSE)

# lookForEmail = re.compile(r"((\w+|\d+)@(\w+|\d+)\.\w{3,4})")
lookForEmail = re.compile(r'''(
    [a-zA-z0-9._%+-]+   #username
    @
    [a-zA-z0-9.&+-]+
    (\.[a-zA-z]{2,4})   #dot something
)''',re.VERBOSE)

phones = lookForPhone.findall(text)

emails = lookForEmail.findall(text)

# print(phones)
# print(emails)

printEmail = []
for i in range(len(emails)) :
    printEmail.append(emails[i][0])
print(f"Emails: "+" | ".join(printEmail))

# printPhone = []
# for i in range(len(phones)) :
#     printPhone.append(phones[i][0])
# print(f"Phone Numbers: "+" | ".join(printPhone))