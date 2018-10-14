from fractions import Fraction
from math import log

T = int(raw_input())

for asdf in xrange(T):
    print "Case #%d:" % (asdf + 1),
    fr = Fraction(raw_input())
    n = fr.numerator
    d = fr.denominator
    m = log(d, 2)
    if m % 1 != 0 or m > 40:
        print "impossible"
        continue
    #print int(m)
    for i in range(41):
        tmp = fr - Fraction(1, 2**i)
        #if i % 20 == 0:
            #print i, fr, repr(tmp)
        if tmp < 0:
            continue
        tmp *= 2**40
        if 0 < tmp < 1:
            continue
        
        if (tmp.denominator == 1):
            print i
            break



