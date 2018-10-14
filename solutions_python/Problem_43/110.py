import sys
import re

inp = open(sys.argv[1])
lines = inp.readlines()
inp.close()

T = int(lines[0])

for i in range(0,T):
    dct = dict()
    x = 1
    second = False
    line = lines[i+1]
    for c in line:
        if c == '\n': continue
        if not c in dct.keys():
            if second:
                dct[c] = 0
                second = False
            else:
                dct[c] = x
                if x == 1:
                    second = True
                x +=1

    base = len(dct)
    if base == 1:
        base = 2
    ret = 0
    for c in line:
        if c == '\n': continue
        ret *= base
        ret += dct[c]
    
    print "Case #%d:" % (i + 1),  ret
                

            

