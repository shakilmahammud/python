import math


def check_prime(n):
    count=0
    for i in range (2, math.floor(math.sqtr(n))+1):
        if n % i == 0:
            print('the number is not prime')
            break
        count = count + 1
    if count+2 == math.floor(math.sqrt(n))+1:
        print('the number is prime')

#n = int(input())
#check_even_odd(n)
