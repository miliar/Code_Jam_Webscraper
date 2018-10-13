import math
import sys

filename = sys.argv[1]
lines = open(filename, 'r')
num = int(lines.readline())

for n in xrange(1, num + 1):
    res = 0
    a, b = map (int, lines.readline().split())
    for i in xrange(a,b+1):
        if str(i) == str(i)[::-1]:
            sq = int(math.sqrt(i))
            if sq**2 == i:
                if str(sq) == str(sq)[::-1]: 
                    res += 1
    print 'Case #'+ str(n)+': ' + str(res)