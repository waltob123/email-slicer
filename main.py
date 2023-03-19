import sys

from email_slicer import email_slicer


def main():
    email = sys.argv[1]
    
    if not email_slicer(email):
        print('Invalid mail')
    else:
        username, domain = email_slicer(email)
        print(f'Your username is {username} and your domain is {domain}', end='\n')


if __name__ == '__main__':
    main()
