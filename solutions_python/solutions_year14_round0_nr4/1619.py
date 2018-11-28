def dwPoint(mi, oth):
    point = 0
    i = 0
    x = len(mi)
    mi.sort()
    oth.sort()
    while i < x:
        j = 0
        y = len(mi)
        while j < y:
            if mi[j] > oth[0]:
                point += 1
                m = mi[j]
                n = oth[0]
                mi.remove(m)
                oth.remove(n)
                break
            j += 1
        i+= 1
    return point
    
def wPoint(mi, oth):
    point = 0
    mi.sort()
    oth.sort()
    mi.reverse()
    i = 0
    x = len(mi)
    while i < x:
        lar = True
        for j in oth:
            if mi[0] < j:
                lar = False
                mi.remove(mi[0])
                oth.remove(j)
                break
        if lar:
            mi.remove(mi[0])
            oth.remove(oth[0])
            point += 1
        i += 1
    return point        
    
    
f = open("a.txt", "r", 0)
t = int(f.readline())
i = 0
while i < t:
    f.readline()
    mi = f.readline().split(' ')
    oth = f.readline().split(' ')
    j = 0
    x = len(mi)
    while j < x:
        mi[j] = float(mi[j])
        j += 1
    j = 0
    x = len(oth)
    while j < x:
        oth[j] = float(oth[j])
        j += 1
    mi1 = mi[:]
    oth1 = oth[:]
    print "Case #" + str(i+1) + ": " + str(dwPoint(mi,oth)) + " " + str(wPoint(mi1,oth1))
    i += 1