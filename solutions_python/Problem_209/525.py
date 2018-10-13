import math

t = int(raw_input(''))
for tc in range(t):
    s = raw_input('')
    s = s.split(' ')
    for i in range(2):
        s[i] = int(s[i])
        
    n = s[0]
    cakes = []
    areas = []
    sdarea = []
    tparea = []
    for i in range(n):
        s1 = raw_input('')
        s1 = s1.split()
        s1[0] = int(s1[0])
        s1[1] = int(s1[1])
        cakes.append(s1)
        top = math.pi*s1[0]*s1[0]
        tparea.append(top)
        side = math.pi*2*s1[0]*s1[1]
        area = top+ side
        areas.append(area)
        sdarea.append(side)
    sdareas = 0
    
    totals = []
    for i in range(n):
        total = 0
        sdareas=0
        top_ar = tparea[i]
        side_tmp = []
        for j in range(n):
            if tparea[j] <= top_ar and j!=i:
                side_tmp.append(sdarea[j])
    #    print side_tmp
        if len(side_tmp) < s[1]-1:
            continue
        for j in range(s[1]-1):
            m = max(side_tmp)
            sdareas += m
            index = side_tmp.index(m)
            del side_tmp[index]
        total = sdareas + areas[i]
        totals.append(total)
    total = max(totals)
    #print sdarea,tparea,areas,totals
    print "Case #" + str(tc+1) + ": " + str(total)

        
        
        
