t = int(raw_input())

for x in xrange(t):
    d, n = map(float, raw_input().split())
    mx = 0
    n = int(n)
    for i in xrange(n):
        dx, nx = map(float, raw_input().split())
        tx = float(d - dx) / nx
        if tx > mx:
            mx = tx
        
    print ("Case #%d: %s" % (x +1, float(d) / mx))
        