#!/usr/bin/python
from math import floor
import decimal

cases = input()
d = decimal.Decimal('3')
s = decimal.Decimal('5')
for case in range(cases):
    exp=input()
    val=int(floor((s**(decimal.Decimal('.5')) + d)**decimal.Decimal(str(exp)) % 1000))
    print "Case #%(case)d: %(val)03d" % {'case':case+1, 'val':val}
