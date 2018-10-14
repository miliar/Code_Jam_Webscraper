from math import *
import sys

f = open(sys.argv[1])

def ispalindrome(n):
    si = str(n)
    lm1= len(si)-1

    if lm1==0:
        return True
    
    for j in range(0, int(ceil(lm1/2.0))):
        if si[j] != si[lm1-j]:
            return False

    return True

numcases = int(f.readline().strip())

for n in range(numcases):
    a,b = [int(tk) for tk in f.readline().strip().split()]
    
    asqrt=int(ceil(sqrt(a)))
    bsqrt=int(floor(sqrt(b)))

    count = 0

    i = asqrt

    while i <= bsqrt:
        
        if ispalindrome(i):
            sq = i*i
            if sq <= b and ispalindrome(sq):
                    #print str(sq) + " is fair and square"
                    count += 1
                    
        i += 1

    print "Case #%s: %s" % (n+1, count)
