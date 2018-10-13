from math import *

def isPalin(a):
    aStr = str(a)
    size = len(aStr)
    for i in range(size/2):
        if(aStr[i] == aStr[size - i - 1]):
            pass
        else:
            return False
    return True

def makePalin(a):
    aStr = list(str(a))
    
    size = len(aStr)
    for i in range(size/2):
        aStr[size - 1 - i] = aStr[i]
    return int(''.join(aStr))

def nextPalin(a):
    while(not isPalin(a)):
        a2 = a
        b = makePalin(a)
        if(b <= a):
            a2 = a + 10**(len(str(a))/2)
            b = makePalin(a2)
        a = b
    return a

def isSqrPalin(a):
    b = a*a
    return isPalin(b)

fairs = int(raw_input())
for f in range(fairs):
    line = raw_input().split(' ')
    low = int(line[0])
    butt = int(ceil(sqrt(low)))
    buttStr = str(butt)
    buttMax = int(floor(sqrt(int(line[1]))))
    #print "bM" + repr(buttMax)
    count = 0
    butt = nextPalin(butt)
    while(butt <= buttMax):
        if(isSqrPalin(butt)):
            count = count + 1
            #print "butts:" + repr(butt) + ":" + repr(butt*butt)
        butt = butt + 1
        butt = nextPalin(butt)
        #print "currConut " + repr(count)
    print "Case #" + repr(f + 1) + ": " + repr(count)
    #find next palendrom
    #loop
    #determine if square is palendrome
    #increment
    #increment butt
    #break if max reached

