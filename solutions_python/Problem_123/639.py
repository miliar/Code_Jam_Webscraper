#Code Jam 2013 - R1A - PA
#Ben Fishbein
#4/13
#Bullseye
#Find how large of a bullseye I can make
#https://code.google.com/codejam/contest/2418487/dashboard#s=p0
##just going for points
###solve large later

from math import *
into = open('CJ2013R1BPA.in')
out = open('CJ2013R1BPA.out', 'w')

Max = 10

def solver(b, A, total):
    count = 0
    for x in range(len(b)):
        if b[x- count] < A:
            A = A + b[x - count]
            b = b[1:]
            count = count + 1
   # print b, "b2", A, total
    if (len(b) == 1 or len(b) == 0):
        total = total + len(b)
        return total
    option1 = solver(b, 2*A -1, total + 1)
    option2 = solver(b[:-1], A, total + 1)
    total = option2
    if(option1 < option2):
        total = option1
    return total




lines = []
lines = into.readlines()
y = 0
while y < (int(lines[0])*2-1):
    a = lines[y+1].split()
    #print a, "a"
    A = int(a[0])
    y = y + 1
    b = lines[y+1].split()
    for x in range(len(b)):
        b[x] = int(b[x])
    b.sort()
    #print b, "b"
    total = 0
    while (len(b) > 0):
        if(A == 1):
            total = len(b)
            break
        count = 0
        for x in range(len(b)):
            if b[x- count] < A:
                A = A + b[x - count]
                b = b[1:]
                count = count + 1
     #   print b, "b2", A
        if (len(b) == 1 or len(b) == 0):
            total = len(b)
            break
        option1 = solver(b, 2*A -1, total + 1)
        option2 = solver(b[:-1], A, total + 1)
        total = option2
        if(option1 < option2):
            total = option1
        break
    y = y + 1
    print  total, "total"
    out.write("Case #" + str(y/2) + ": " + str(total) + "\n")
out.close()


