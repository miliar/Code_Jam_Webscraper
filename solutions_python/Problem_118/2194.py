# fairnsquare1.py

##Input
##3
##1 4
##10 120
##100 1000
##
##Output
##Case #1: 2
##Case #2: 0
##Case #3: 2

import math

def is_palindrome(num):
    num = str(num)
    slen = len(num)
    for i in range(0, slen // 2):
        if num[i] != num[-1-i]:
            return False
    return True

def is_square_of_palindrome(num):
    until = int(math.sqrt(num)) + 2
    for i in range(1, until):
        if i * i == num and is_palindrome(i):
            return True
    return False

# main

fin = open("C-small-attempt0.in", 'r')
fout = open("C-small-attempt0.out", 'w')

T = int(fin.readline())
lines = fin.readlines()

i = 1
for line in lines:
    bounds = line.split()
    A = int(bounds[0])
    B = int(bounds[1])
    n = 0
    for k in range(A, B+1):
        if is_palindrome(k) and is_square_of_palindrome(k):
            n = n + 1
    fout.write("Case #{}: {}\n".format(str(i), str(n)))
    i = i + 1
    
fin.close()
fout.close()
