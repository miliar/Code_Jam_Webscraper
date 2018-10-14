import sys
import math

lines = sys.stdin.readlines()
tc = int(lines[0].strip())
lines = lines[1:]

for i in range(0, tc):
    m, n = lines[i].split()
    m = int(math.ceil(math.sqrt(int(m))))
    n = int(math.sqrt(int(n))) + 1
    #print "m, n = ", m, n
    count = 0
    for j in range(m, n):
        sqare = j * j
        sj = str(j)
        ss = str(sqare)
        if sj[::-1] == sj and ss[::-1] == ss:
            count += 1
    print "Case #%d: %d" % (i + 1, count)
