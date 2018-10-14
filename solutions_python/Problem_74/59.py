# -*- coding: utf-8 -*-
from itertools import *
   
import sys
fin = sys.stdin
N = int(fin.readline())
for case in range(1,N+1):
    line = fin.readline().split()
    data = zip(line[1::2], map(int, line[2::2]))
    
    op = 1
    ot = 0
    bp = 1
    bt = 0
    for user, position in data:
        if user == 'O':
            ot = max(ot+abs(position-op), bt)+1
            op = position
        else:
            bt = max(bt+abs(position-bp), ot)+1
            bp = position
    
    print "Case #%d: %s" % (case, max(ot, bt))
