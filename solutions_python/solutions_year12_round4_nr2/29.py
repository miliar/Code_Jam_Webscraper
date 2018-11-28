################################################################
def solve():
    N,W,L = [int(x) for x in input.readline().split(' ')]
    r = [int(x) for x in input.readline().split(' ')]
    r_with_orig = [(r[i],i) for i in range(N)]
    r_with_orig.sort()
    r_with_orig.reverse()

    x,y = 0,0
    placements = range(N)
    for (radius,i) in r_with_orig:
        if (x,y) == (0,0):
            placements[i] = (0,0)
            x = radius
            next_y = y+radius
        elif x == 0:
            placements[i] = (0,y+radius)
            next_y = y+2*radius
            x = radius
        elif y == 0 and x+radius <= W:
            placements[i] = (x+radius,0)
            x += 2*radius
        elif x+radius <= W:
            placements[i] = (x+radius,y+radius)
            x += 2*radius
        else:
            (x,y) = (0, next_y)
            placements[i] = (0,y+radius)
            next_y = y+2*radius
            x = radius

    for (i,j) in placements:
        if i > W or j > L:
            print "YOU BLEW IT"
            print placements
            die

    return " ".join(["%s %s" % (i,j) for (i,j) in placements])

################################################################

from datetime import datetime
time_start = datetime.today()
def now(): return datetime.today() - time_start 

import sys
infilename = sys.argv[1]
outfilename = infilename.replace('.in','.out')

input = open(sys.argv[1], 'r')
output = open(sys.argv[1].replace('.in','.out'), 'w')
n = int(input.readline())

for i in range(1,n+1):
    result = solve()
    print "Case #%d: %s \t %s" % (i, result, now())
    output.write("Case #%d: %s\n" % (i, result))
    output.flush()
