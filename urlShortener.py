## Author: Joseph Sepich
## DS 220 HW 2
## March 31, 2019
## URL Shortener Implemented with Redis
import redis
import random
import string

# Set Up Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# r.set('key', 'value')
# r.get('key')

stringSize = 5

# Keep track of values
keys = []

# Read URLs to be shortened
while True:
    print('Welcome to https://shorten.com')
    print('Type insert <URL> to insert')
    print('Type retrieve <key> to get URL')
    print('Type keys to get all keys')
    print('Type exit to exit')
    userInput = input()
    userInput = userInput.split(' ')
    command = str(userInput[len(userInput) - 2])
    value = str(userInput[len(userInput) - 1])
    print(value)
    if command == 'exit':
        break
    elif command == 'keys':
        print(keys)
    elif command == 'retrieve':
        value = value[value.rfind('/') + 1:len(value)]
        print(value)
        value = str(r.get(value))
        value = value[1:len(value)]
    elif command == 'insert':
        rand = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(stringSize))
        while rand in keys:
            rand = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(stringSize))
        keys.append(rand)
        r.set(rand, value)
        print('New URL for ' + value + ' is https://shorten.com/' + rand)
    else:
        print('Please enter a valid command')
    print('')
    print('------------------------------------------------')
    print('------------------------------------------------')
    print('')

