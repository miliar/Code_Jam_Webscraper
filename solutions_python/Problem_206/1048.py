t = int(raw_input())

for i in xrange(1, t+1):
    d, n = map(int, raw_input().split())
    currMax = 0.0

    for j in range(n):
        k, s = map(int, raw_input().split())
        curr = (d - k) * 1. / s

        if curr > currMax:
            currMax = curr

    #print('Case #{0}: {1}'.format(i, d / currMax))
    print ('Case #%d: %.6f' %(i, d/currMax))
