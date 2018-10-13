import sys
for t in range(int(sys.stdin.readline())):
    smax, s = sys.stdin.readline().split()
    smax = int(smax)
    s = [int(s[i]) for i in range(len(s))]
    n = 0 # number of people standing
    y = 0 # number of friends needed
    for k in range(smax + 1):
        if n < k:
            y += k - n
            n += k - n
        n += s[k]
    print 'Case #%d: %d' % (t + 1, y)
    
