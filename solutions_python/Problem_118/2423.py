import math

__author__ = 'wonglik'

def reverse(s):
    rev = ''

    for ch in s:
        rev = ch +rev

    return rev

def is_palindrome(num):

    s = str(num)
    n = len(s)

    return s[:n //2 ] == reverse(s[n - n//2:])


def fair_and_square(m,n):

    count = 0
    upper_limit = int(math.floor(math.sqrt(n)))
    lower_limit = int(math.ceil(math.sqrt(m)))
    for x in xrange(lower_limit,upper_limit+1):
        if is_palindrome(x) and is_palindrome((x)*(x)):
            count = count +1

    return count




f = open('C-small-attempt0.in', 'r')
fw = open('output', 'w')

lines = f.readlines()

cases = int(lines[0].strip())
lines= lines[1:]

for idx,line in enumerate(lines):
    m,n = map(int,line.strip().split(" "))
    count =  fair_and_square(m,n)
    fw.write("Case #"+str(idx+1)+": "+str(count))
    fw.write('\n')

f.close()
fw.close()



