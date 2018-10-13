
'''

given x

if x is palin and square:
    if sqrt(x) is palin:
        yes
    else
        no

'''
########################3

import math

def palin(x): # check if a number is a palindrome
    return str(x) == str(x)[::-1]


def square(x): # check if a number is a square
    import math
    return math.sqrt(x) == int(math.sqrt(x))


T = int(raw_input())



for i in range(T):

    c = 0 # counter

    A,B = (int(x) for x in raw_input().split())

    for j in range(A,B+1):
        if palin(j) and square(j):
            if palin(int(math.sqrt(j))):
                c += 1


    print 'Case #%d: %d' % (i+1, c)
        



