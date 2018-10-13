T = input()
for t in range(T):
    C, F, X = [float(x) for x in raw_input().split()]
    x = 0
    time2GetX = 0
    rate = 2
    fCost = iCost = time2GetX + (X/rate)
    while(fCost<=iCost):
        iCost = fCost
        x = x+1
        time2GetX = time2GetX + (C/rate)
        rate = 2 + (x*F)
        fCost = time2GetX + (X/rate)
        
    print "Case #%d: %f" % (t+1, iCost)


