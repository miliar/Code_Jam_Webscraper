#!/usr/bin/python

import math
import decimal
from decimal import Decimal

in_file = "C-small-attempt0.in"
out_file = "C-small-attempt0.out"

try:
    f_in = open(in_file)
except IOError:
    print in_file, "can not be opened, plz check it out!"
    
try:
    f_out = open(out_file,"w+")
except IOError:
    print out_file, "can not be opened, plz check it out!"    
    

T = int(f_in.readline())

a = Decimal('5.2360679774997896964091736687307902146760825424117459425048075327691066149782272987067699432373046875')
decimal.getcontext().prec=200
for i in range(0,T):
    n = int(f_in.readline())
    b = str(a ** n)
    print b
    index = b.index('.')
    result = b[:index]
    result = result[-3:]
    f_out.write("Case #" + str(i+1) + ": ")
    if len(result)< 3:
        for j in range(0, 3-len(result)):
            f_out.write("0")
    f_out.write(result + "\n")
    
f_in.close()
f_out.close()





