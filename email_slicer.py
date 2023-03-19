import re

def email_slicer(email):
    '''
    This function takes an email as input and returns the
    username and domain of the email.
    '''
    
    pattern = r"(^[a-zA-Z][a-zA-Z0-9.-]+)@([a-zA-Z]+.[a-zA-Z]+$)"
    result = re.search(pattern, email)
    
    # check if result is None or not
    if result is None:
        return False
    return result.groups()
