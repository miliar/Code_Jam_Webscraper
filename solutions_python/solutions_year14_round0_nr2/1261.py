#!/usr/bin/python

from decimal import *

getcontext().prec = 200

def test(t, o, caseNum):
    c = Decimal(t[0])
    f = Decimal(t[1])
    x = Decimal(t[2])
    r = Decimal(2.0)
    timer = Decimal(0.0)

    while 1:
        timeFarm = c / r
        timeEnd = x / r

        tmpRate = r + f

        timeEndNew = x / tmpRate

        if timeEnd < timeEndNew + timeFarm:
            timer = timer + timeEnd
            break

        r = r + f
        timer = timer + timeFarm

    num = str(round(timer, 7))
    #o.write(num + '\n')
    o.write('Case #' + str(caseNum) + ': ' + num + '\n')

#fileIn = open("q.in")
fileIn = open("/Users/tony/Downloads/B-large.in.txt")
i = fileIn.readline()
o = open("a.out", 'w')
i = int(i)

for k in xrange(0, i):
    x = fileIn.readline().split()
    test(x, o, k + 1)
    print k

