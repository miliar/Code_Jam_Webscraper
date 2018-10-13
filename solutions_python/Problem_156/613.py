for ca in xrange(input()):
    n = input()
    vs = map(int, raw_input().split(' '))
    ma = max(vs)
    ans = ma
    for h in xrange(1, ma + 1):
        acc = h
        for v in vs:
            acc += (v + h - 1) / h - 1
        ans = min(ans, acc)
        
    print "Case #" + str(ca + 1) + ": " + str(ans)

        
