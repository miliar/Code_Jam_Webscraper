import sys

a = [[] for j in xrange(10)]

for i in xrange(1, 1+int(sys.stdin.readline())):
    l = sys.stdin.readline().replace("\n", "").split(" ")
    grass = []
    N, M = map(int, l)
    cancutline = [True for n in xrange(N)]
    cancutrow = [True for m in xrange(M)]


    for n in xrange(N):
        l = sys.stdin.readline().replace("\n", "").split(" ")
        grass.append(map(int, l))

    for n in xrange(N):
        onecount = grass[n].count(1)
        twocount = grass[n].count(2)
        if twocount > 0:
            cancutline[n] = False

    for m in xrange(M):
        t = [grass[x][m] for x in xrange(N)]
        onecount = t.count(1)
        twocount = t.count(2)
        if twocount > 0:
            cancutrow[m] = False

    possible = True
    for n in xrange(N):
        for m in xrange(M):
            if grass[n][m] == 1:
                if not cancutline[n] and not cancutrow[m]:
                    possible = False

    s = "YES" if possible else "NO"
    print "Case #%d: %s" % (i, s)
