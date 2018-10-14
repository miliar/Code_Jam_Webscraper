
import sys
from decimal import *
getcontext().prec = 1000

base = Decimal(3) + Decimal(5).sqrt()

def proc(num):
    prod = base ** num
    string = str(int(prod))
    parte = string[-3:].zfill(3)
    return parte
        

archinp = open(sys.argv[1])
canttests = int(archinp.readline())

for numtest in xrange(1,canttests+1):
    num = int(archinp.readline())
    result = proc(num)
    print "Case #%d: %s" % (numtest, result)
