import math
inf = open("in.txt", "r")
ouf = open('out.txt','w')

def close_files():
    inf.close
    ouf.close

def precount():
    pass
            
printcounter = 0
def printstr(s):
    global printcounter
    printcounter +=1
    print >>ouf, 'Case #%d: %s' % (printcounter, s)

def gcd(a,b):
    c = a
    d = b
    while c > 0:
        c, d = d %c, c
    return c+d

def solvetest():
    a, b = map(int, inf.readline().split())
    l = len(str(a))
    m = pow(10, l-1)
    count = 0
    for i in xrange(a, b+1):
        if i >= (m * 10):
            m *= 10
            l += 1
        tmp = i
        s = set();
        for j in xrange(1, l):
            tmp = (tmp % 10)*m + (tmp / 10)
            if (tmp > i) and (tmp <= b) and (tmp not in s):
                count += 1
                s.add(tmp)
    printstr(count)
         
precount()
testnum = int(inf.readline())
for test in xrange(testnum):
    solvetest()
close_files()

