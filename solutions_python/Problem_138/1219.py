import bisect

trials = int(raw_input())

for i in range(1, trials+1):
    size = int(raw_input())
    girl = map(float, raw_input().split())
    boy = map(float, raw_input().split())
    
    boy.sort()
    girl.sort()
    
    boyreal = boy[:]

    dPoints = 0
    wPoints = 0
    
    for x in range(size):
        bigger = True
            
        for y in range(len(girl)):
            if (girl[y] < boy[y]):
                bigger = False
    
        glow = min(girl)
        girl.remove(min(girl))
        
        bhigh = max(boy)
        blow = min(boy)
        
        bpos = bisect.bisect(boyreal, glow)
        if bpos >= len(boyreal):
            bpos = 0

        bclose = boyreal[bpos]
        boyreal.remove(bclose)

        if not bigger:
            gfake = bhigh - .0000001
            bchoice = bhigh
        else:
            gfake = blow  + .0000001
            bchoice = blow

        boy.remove(bchoice)
        
        if glow > bclose:
            wPoints += 1
        
#        print "Girl says she has " + str(gfake)
#        print "Boy plays " + str(bchoice)
#        print "Girl really played " + str(glow)
#        print ""

        if glow > bchoice:
            dPoints += 1

    print "Case #" + str(i) + ": " + str(dPoints) + " " + str(wPoints)

