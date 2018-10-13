import itertools
import sys
import math

f = sys.stdin

ncases = int(f.readline().strip())

def palin(n):
    return str(n) == str(n)[::-1]

for case in xrange(ncases):
    line = f.readline().strip().split(' ')
    A = long(line[0])
    B = long(line[1])
    count = 0
    for n in range(B+1):
        if palin(n):
            sq = n**2
            if (sq <= B) and (sq >= A) and palin(sq):
                count = count + 1
    print "Case #" + str(case+1) + ": " + str(count)
