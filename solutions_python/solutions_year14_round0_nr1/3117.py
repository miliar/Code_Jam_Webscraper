#!/usr/bin/env python
from itertools import islice

f = open('A-small-attempt0.in')

t = int(f.readline())

for i in xrange(t):
    ans1 = int(f.next())
    grid1 = ' '.join(list(x.strip() for x in islice(f, 4)))
    ans2 = int(f.next())
    grid2 = ' '.join(list(x.strip() for x in islice(f, 4)))
   
    grid1 = [int(x) for x in grid1.split(' ')]
    grid2 = [int(x) for x in grid2.split(' ')]

    a1 = set(grid1[(ans1-1)*4:ans1*4])
    a2 = set(grid2[(ans2-1)*4:ans2*4])

    a = a1.intersection(a2)

    if len(a) > 1:
        soln = "Bad magician!"
    elif len(a) == 0:
        soln = "Volunteer cheated!"
    else:
        soln = a.pop()

    print "Case #%d: %s" % (i+1, soln) 

f.close()
