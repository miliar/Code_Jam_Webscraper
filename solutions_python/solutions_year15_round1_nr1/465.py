import sys

for tc in range(1, 1 + int(sys.stdin.readline())):
    N  = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    vals = line.split(" ")
    intvals = map(int, vals)

    eaten1 = 0
    maxdiff = 0
    for n in xrange(1,N):
        currdiff = max(0, intvals[n-1] - intvals[n])
        eaten1 += currdiff
        maxdiff = max(maxdiff, currdiff)




    eaten2 = 0
    for n in xrange(N-1):
        if intvals[n] > 0:
            eaten2 += min(maxdiff, intvals[n])





    res = "%d %d" % (eaten1, eaten2)
    print "Case #%d: %s" % (tc, res)



