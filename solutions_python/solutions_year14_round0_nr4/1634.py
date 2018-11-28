n = input()
for iii in xrange(n):
    c = input()
    naomi = map(float, raw_input().split())
    naomi.sort()
    ken = map(float, raw_input().split())
    ken.sort()
    dwin = 0
    tempken = list(ken)
    for i in xrange(c):
        if naomi[i] < tempken[0]:
            tempken.remove(tempken[-1])
        else:
            tempken.remove(tempken[0])
            dwin += 1
    nwin = c
    tempken = list(ken)
    for i in naomi:
        for j in tempken:
            if j > i:
                nwin -= 1
                tempken.remove(j)
                break
    print 'Case #%d: %d %d' % (iii+1, dwin, nwin)
                
