import sys

t = int(sys.stdin.readline().strip())
for ti in xrange(t):
    line = sys.stdin.readline().split()
    n = int(line[0])
    k = int(line[1])

    m = 1
    while k > (1 << m) - 1:
        m += 1
    
    if (1 << m) > n:
        y, z = 1, 1
    else:
        z = (n + 1) / (1 << m)
        d = (n + 1) - z * (1 << m)
        if k <= (1 << (m - 1)) - 1 + d:
            y = z + 1            
            if k <= (1 << (m - 1)) - 1 + d - (1 << (m - 1)):
                z = y
        else:
            y = z

    print 'Case #%d: %d %d' % (ti + 1, y - 1, z - 1)
        
