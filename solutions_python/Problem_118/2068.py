from math import sqrt

def isSquare(n):
    t = (int)(sqrt(n))
    return t*t == n

def isPalindrome(n):
    s = (str)(n)
    start = 0
    end = len(s) - 1
    while (start < end):
        if (s[start] != s[end]):
            return False
        start += 1
        end -= 1
    return True

f = open('C-small-attempt0.in','r')
g = open('C-small.out','w')
a = f.read()
b = a.split('\n')

cases = (int)(b[0])

for i in range(0,cases):
    t = b[i+1].split(' ')
    s = (int)(t[0])
    e = (int)(t[1])
    count = 0
    for j in range(s,e+1):
        if (isPalindrome(j) and isSquare(j) and isPalindrome((int)(sqrt(j)))):
            count += 1

    g.write("Case #"+(str)(i+1)+": " + (str)(count) + "\n") 

f.close()
g.close()
