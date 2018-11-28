import sys

with open(sys.argv[1]) as ff:
    t = int(ff.readline())
    for c in range(1,t+1):
        n, x = map(int,ff.readline().split())
        s = sorted(map(int,ff.readline().split()))
        total = 0
        while len(s) >= 2:
            big = s.pop(-1)
            if s[0] + big <= x:
                s.pop(0)
            total += 1
        total += len(s)
        print "Case #%d: %d" % (c,total)