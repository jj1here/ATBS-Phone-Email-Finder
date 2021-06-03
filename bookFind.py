import pyperclip
import re

# copies
# Call me at 512-233-1233 tomorrow. 401-421-4214 is my office.
# Find me at aSd@das.net tomorrow. Also 32k32@asd7a.com is my office.
# Call me at 512-233-1233 tomorrow. Also fasFs@ds3d.att is my office.

text = str(pyperclip.paste())
print(text)
print()

# lookForPhone = re.compile(r"\d{3}-\d{3}-\d{4}")
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?
    (\s|-|\.)?
    (\d{3})
    (\s|-|\.)
    (\d{4})
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  #extension
)''',re.VERBOSE)

# lookForEmail = re.compile(r"((\w+|\d+)@(\w+|\d+)\.\w{3,4})")
emailRegex = re.compile(r'''(
    [a-zA-z0-9._%+-]+   #username
    @
    [a-zA-z0-9.&+-]+
    (\.[a-zA-z]{2,4})   #dot something
)''',re.VERBOSE)

   # Find matches in clipboard text.

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
       matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')

