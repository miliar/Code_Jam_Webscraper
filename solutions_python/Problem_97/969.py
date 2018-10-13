import sys
import math

def mycount(a, b, row):
    seen = set()
    def countdup(i):
        digits = int(math.log(i) / math.log(10))
        cnt = 0
        localvalidcount = 0
        for n in xrange(digits):
            i = i%10 * 10**digits + i / 10
            if a <= i <= b and not i in seen:
                seen.add(i)
                localvalidcount += 1
                cnt += localvalidcount
        return cnt
    
    totaldup = 0
    for i in xrange(a, b+1):
        if i in seen:
            continue
        seen.add(i)
        totaldup += countdup(i)
    print "Case #%s: %s" % (row, totaldup)

fd = open(sys.argv[1])
n = fd.readline()
for n, l in enumerate(fd.readlines()):
    a, b = [int(i) for i in l.split()]
    mycount(a, b, n+1)
