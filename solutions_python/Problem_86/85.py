T = input()
for caso in range(T):
    N, L, H = map(int, raw_input().split())
    f = map(int, raw_input().split())
    
    res = L;
    while res <= H:
        b = True
        for n in f:
            if res % n != 0 and n % res != 0:
                b = False
                break
        if b:
            break
        else:
            res += 1
    
    if res <= H:
        print "Case #%s: %s" % (caso+1, res)
    else:
        print "Case #%s: NO" % (caso+1)
