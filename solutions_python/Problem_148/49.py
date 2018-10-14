__author__ = 'dan'

T = int(raw_input())
for case in range(1, T+1):
    n, x = map(int, raw_input().split())
    disks = sorted(map(int, raw_input().split()))
    count = 0
    u, v = 0, n-1
    while u < v:
        if disks[u] + disks[v] <= x:
            count += 1
            u += 1
            v -= 1
        else:
            count += 1
            v -= 1
    if u == v:
        count += 1

    print "Case #%d: %d" % (case, count)







