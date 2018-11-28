T = input()
for t in range(1,T+1):
    Smax, aud = raw_input().split()
    aud = map(int, aud)
    y, s = 0, 0
    for i, e in enumerate(aud):
        if s + y < i: y = i - s
        if e: s += e
    print "Case #{}: {}".format(t, y)
        
