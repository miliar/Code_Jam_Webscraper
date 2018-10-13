#!/usr/bin/env python
import sys
import numpy as np

def get_digits(number):
    ndigits=int(np.log10(number))+1
    digits=np.zeros(ndigits)
    for i in xrange(ndigits):
        digits[i]=int(number/10**(ndigits-i-1))
        number-=digits[i]*10**(ndigits-i-1)
    return digits.astype(int)

def is_tidy(number):
    digits = get_digits(number)
    a = np.sort(digits)
    #print digits, a
    if (digits==a).all():
        return True
    else:
        return False
def get_result(number):
    while not is_tidy(number):
        number-=1
    return number
   

if __name__=='__main__':
    infile = sys.argv[1]
    fin = open(infile,mode='r')
    Ncase = int(fin.readline().rstrip())
    for i in xrange(Ncase):
        line = fin.readline().rstrip()
        result = get_result(int(line))
        print "Case #%d: %s" % (i+1, result)



