import re # module for processing regular expressions https://docs.python.org/3/library/re.html

# Initial prompt to user
line = input("Enter a phone number to validate or 'exit' when done. ")

# TODO Define your regex
entirePhoneRegex = '^\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$'

removeNonIntRegex = '\d'
while line != "exit":
    # TODO Find matches
    matchObj = re.search(entirePhoneRegex, line)
    
    
    if not matchObj: 
        # TODO If no match found, print that no number was found
        print('No valid number found')
    else:
        #match found
        # TODO Else, break number up into area code, prefix, and suffix
        myMatch = matchObj.group(0)
        print(myMatch)
        phoneNum = re.sub('[^0-9]','' ,myMatch)
        print(phoneNum)

        #get area code
        areaCode = phoneNum[:3]
        #get prefix
        prefix = phoneNum[3:6]
        #get suffix
        suffix = phoneNum[6:]
        
        print(f'Area Code: {areaCode}, Prefix: {prefix}, Suffix: {suffix}')

    
    # As a stretch goal, you can modify your regex to search for country codes
    # too and print that out as well!
    
    
    # Done validating, read in a new line
    line = input("Enter a phone number to validate or 'exit' when done. ")
