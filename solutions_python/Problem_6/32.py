import sys

import math
from decimal import *

input_line = open(sys.argv[1], 'r').read().strip().split('\n')
testcase_no = int(input_line.pop(0))
out_fp = open(sys.argv[2], 'w')

print "testcase_no %s"%(testcase_no)

def parse_testcase(lines):
    return int(lines.pop(0))

getcontext().prec = 100
five_sqrt = getcontext().sqrt(Decimal(5))
for cur in range(testcase_no):
    
    num = parse_testcase(input_line)
    
#    result2 = math.pow((3 + math.sqrt(5)), num)%1000
#    
#    pow_set = 9 + 2*3*math.sqrt(5) + 5
#
#    result = pow_set*(num/2)
#    
#    if (num%2 != 0):
#        result *= (3+math.sqrt(5))
#
#    s = int(result)%1000
#    mo = str(s)
#    if len(mo) < 3:
#        mo2 = "0"*(3-len(mo))
#        mo2 += mo
#        mo = mo2

#    decimal.getcontext().prec = 1000
#    two = decimal.Decimal("2")
#    five_sqrt = decimal.getcontext().sqrt(two)
#    pow_set = decimal.Decimal("14") + decimal.Decimal("6")*five_sqrt
#
#    result = pow_set*decimal.Decimal(num/2)
#
#    if (num%2 != 0):
#        result *= (decimal.Decimal("3")+five_sqrt)
#
#    print (decimal.Decimal("3")*five_sqrt)
#    x = decimal.getcontext().power((decimal.Decimal("3")*five_sqrt), decimal.Decimal(num))
#    print x
#
##    print two
##    print five_sqrt
#    print result

#    pow_set = Decimal("14") + Decimal("6")*five_sqrt
#    print five_sqrt
#    print getcontext().power(Decimal("3")+five_sqrt, 1)
#    print math.pow((3 + math.sqrt(5)), 1)
    mo = str(getcontext().power(Decimal("3")+five_sqrt, num))
    mo = mo[:mo.index('.')]
    if len(mo) < 3:
        mo2 = "0"*(3-len(mo))
        mo2 += mo
        mo = mo2
    elif len(mo) > 3:
        mo = mo[-3:]

#    print result
#    print result2
#    print s
#    print mo
    print "Case #%i: %s"%(cur+1, mo)
    out_fp.write("Case #%i: %s\n"%(cur+1, mo))

