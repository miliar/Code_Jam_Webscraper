#!/usr/bin/python

import sys

for n,line in enumerate(open(sys.argv[1])):
    if n==0:
        continue
    if n%2==1:
        continue
    
    te=[int(x) for x in line.split()]
    
    no=False
    for s in range(0,22):
        a=len([x for x in te if (x & (1<<s)) != 0 ])
        if a % 2 != 0:
            no=True
    
    if no:
        print("Case #{0}: {1}".format(n//2,"NO"))
    else:
        print("Case #{0}: {1}".format(n//2,sum(te)-min(te)))

