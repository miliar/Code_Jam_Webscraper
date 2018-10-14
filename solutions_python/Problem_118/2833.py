from math import *

def palindrome(n):
    string = str(n)
    if string == string[::-1]:
        return True
    return False

n = int(raw_input())

for i in range(n):
    [a, b] = raw_input().split()
    a=int(a)
    b = int(b)

    high = int(ceil(sqrt(b)))
    low = int(sqrt(a))

    list = []
    for j in range(low, high+1):
        if palindrome(j):
            list.append(j*j)

    fairsquare = 0
    for k in list:
        if palindrome(k):
            if k>=a and k<=b :
                fairsquare = fairsquare + 1
    print "Case #"+str(i+1)+": "+str(fairsquare)
    

