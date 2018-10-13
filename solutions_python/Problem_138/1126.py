import sys

f = open(sys.argv[1])
T = int(f.readline())
for t in xrange(1,T+1):
    n = int(f.readline().strip())

    pl0 = map(float, f.readline().strip().split())
    pl1 = map(float, f.readline().strip().split())
    pl0.sort()
    pl1.sort()

    y, z = 0, n
    j = 0
    for i in range(n):
        if pl0[i] > pl1[y]:
            y += 1
        if pl0[n-i-1] < pl1[z-1]:
            z -= 1

    print "Case #{0}: {1} {2}".format(t, y, z)
