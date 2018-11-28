T = input()
for t in xrange(T):
    c,f,x = map(float, raw_input().split())
    v = 2
    r = x/2
    time = 0
    while time < r:
        time += c/v
        v += f
        r = min(r, time + x/v)
    print 'Case #%d: %.9f' % (t+1, r)
