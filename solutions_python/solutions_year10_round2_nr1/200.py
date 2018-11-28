import sys
import os

def getnum():
    return [int(x) for x in sys.stdin.readline().split()]

C, = getnum()

for i in range(1, C+1):
    N, M = getnum()
    dirs = []

    for n in range(N):
        d = sys.stdin.readline()[1:-1]
        assert d[0] != '/'
        os.system("mkdir -vp %s > /dev/null" % d)
        dirs.append(d)

    sol = 0
    for m in range(M):
        d = sys.stdin.readline()[1:-1]
        assert d[0] != '/'
        x = os.system("mkdir -vp %s | wc -l > tmp" % d)
        with open("tmp") as f:
            x = int(f.read())
        sol += x
        dirs.append(d)

    print "Case #%d: %d" % (i, sol)

    for d in sorted(dirs):
        os.system("rmdir -p %s 2>/dev/null >/dev/null" % d)
    dirs = []
