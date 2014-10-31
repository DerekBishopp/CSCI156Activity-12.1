__author__ = 'Derek'

def emailthing():
    x = input('Enter Email: ')
    username,domain = x.split('@')
    domain,gTLD = domain.split('.')
    #print(y)
    #print(l)
    print('Username: ', username)
    print('Domain: ', domain)
    print('gTLD: ', gTLD)

emailthing()