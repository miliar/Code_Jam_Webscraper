import math
import decimal
f = open("/Users/hugh/Desktop/Personal/projects/80days/r1/samll-in-c.txt")
for i in range(1,int(f.readline())+1):
#for i in range(1,31):
    value = int(f.readline())
#    value = i
    result = str(int((decimal.Decimal('5').sqrt() + 3)**value))
    value= result[-3:len(result)]
    if len(value) < 3:
        value = '0'*(3-len(result)) +value
    print 'Case #%d: %s'% (i, value)
