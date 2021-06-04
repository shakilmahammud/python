year = int(input('enter the number'))

if year % 400 == 0:
    print('it is a lipyear')
elif year % 100 == 0:
    print('it is not lip year')
elif year % 4 == 0:
    print('it is a lipyear')
else:
    print('it is not lip year')
