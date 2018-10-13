from decimal import *

def getChars(n):
    foo = Decimal(5)
    base = Decimal(3+foo.sqrt())
    product = Decimal(1)
    return "%03d" % int(base**n % 1000)
    
'''    while n>0:
        if n%2==1:
            product *= base
            n -= 1
        else:
            base *= base
            n /= 2
        product %= 1000
        base %= 1000
    
    return "%03d" % int(product)'''

getcontext().prec = 1000

n = int(raw_input())

for case in xrange(n):
    input = int(raw_input())
    print "Case #%d: %s" % (case+1,getChars(input))
