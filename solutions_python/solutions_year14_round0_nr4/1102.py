#! /usr/bin/python

import sys, bisect


if len(sys.argv) < 2:
    print("Usage: ./p1.py <input file>")
    sys.exit(1)

try:
    fin = open(sys.argv[1])
except IOError:
    print("Input file not found")
    sys.exit(1)

data = fin.readlines()
fin.close()
ind = 1
num = int(data[0].strip())

for q in xrange(num):
    n = int(data[ind].strip())
    naomi = data[ind+1].strip().split()
    naomi = map(float, naomi)
    naomi.sort()
    ken = data[ind+2].strip().split()
    ken = map(float, ken)
    ken.sort()
    optimalscore = 0
    cheatingscore = 0

    #Cheating:
    while n > 0:
        if n == 1:
            if naomi[0] > ken[0]:
                cheatingscore += 1
        elif naomi[0] > ken[0]: #Pop off two smallest blocks
            cheatingscore += 1
            del naomi[0]
            del ken[0]
        else:
            #Force Ken to get rid of his largest block
            del naomi[0]
            del ken[-1]
        n -= 1

    #Optimal:
    n = int(data[ind].strip())
    naomi = data[ind+1].strip().split()
    naomi = map(float, naomi)
    naomi.sort()
    ken = data[ind+2].strip().split()
    ken = map(float, ken)
    ken.sort()
    ind += 3
    while n > 0:
        block = naomi.pop()
        if block > ken[-1]:
            del ken[0]
            optimalscore += 1
        else:
            i = bisect.bisect_left(ken, block)
            del ken[i]
        n -= 1
    print "Case #%d: %d %d"%(q+1,cheatingscore,optimalscore)
sys.exit(0)
