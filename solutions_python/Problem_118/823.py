import sys
from math import sqrt

def case(a,b):
    lower = int(sqrt(a))
    upper = int(sqrt(b))
    current = lower
    count =0
    current = make_palindrome(current)
#    print(lower,upper)
    while current<=upper:
#        print(current,current**2)
        if(current**2 >= a):
            count += check_palindrome(current**2)
        strcurrent = str(current)
        digits = len(strcurrent)
        mid = int(digits/2)
        current += 10**(mid)
        current = make_palindrome(current)
    print(count)

def make_palindrome(n):
    strn = str(n)
    digits = len(strn)
    if digits == 1:
        return n

    n = 0
    if digits % 2 == 0:
        for i in range(int(digits/2)):
            n += (10**i)*int(strn[i])
            n += (10**(digits-i-1))*int(strn[i])
    else:
        n+= (10**(int(digits/2)))*int(strn[int(digits/2)])
        for i in range(int(digits/2)):
            n += (10**i)*int(strn[i])
            n += (10**(digits-i-1))*int(strn[i])

    return n

def check_palindrome(n):
    strn = str(n)
    digits = len(strn)
    for i in range(int(digits/2)):
        if (strn[i] != strn[digits-i-1]):
            return 0
    return 1

def work(fin):
    t = int(fin.readline())
    for i in range(t):
        lawn = []
        print("Case #",i+1,": ",end="",sep="")
        temp = fin.readline().split()
        a,b = int(temp[0]),int(temp[1])
        case(a,b)

if __name__ == "__main__":
    INPUT = sys.argv[1]

    fin = open(INPUT,'r')
    work(fin)
