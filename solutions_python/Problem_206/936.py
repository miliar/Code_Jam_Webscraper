import sys

t = int(sys.stdin.readline())

for i in range(1, t + 1):
    dn = sys.stdin.readline().split(' ')
    d = int(dn[0])
    n = int(dn[1])
    maxdesttime = 0
    for j in range(n):
        ks = sys.stdin.readline().split(' ')
        k = int(ks[0])
        s = int(ks[1])
        desttime = (d - k) / s
        if maxdesttime < desttime:
            maxdesttime = desttime

    print('Case #{0}: {1:.6f}'.format(i, d / maxdesttime))
