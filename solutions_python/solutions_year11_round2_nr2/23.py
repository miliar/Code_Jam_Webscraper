f = open('B-large.in','r')
out = open('largeoutput.txt','w')

numcases = int(f.readline())

for casenum in range(numcases):
    
    vals = f.readline().split(' ')
    
    pointsWithVendors = int(vals[0])
    d = int(vals[1])
    
    allVendors = []
    totalTraveled = []
    
    for p in range(pointsWithVendors):
        vals = f.readline().split(' ')
        
        p = int(vals[0])
        v = int(vals[1])
        
        for vendor in range(v):
            allVendors.append(p)
            totalTraveled.append(0)
    
    allVendors.sort()
    
    while(True):
        keepGoing = False
        for v in range(len(allVendors)-1):
            if(allVendors[v+1] - allVendors[v] < d):
                keepGoing = True
                break
        if(not keepGoing):
            break
        
        v = len(allVendors)-2
        while(v >= 0):
            dist = allVendors[v+1] - allVendors[v]
            if(dist < d):
                allVendors[v] -= (d - dist)
                totalTraveled[v] += (d - dist)
            v -= 1
        
        #print allVendors
    
    time = max(totalTraveled) / 2.0
    
    out.write('Case #%d: %f\n' % ((casenum+1), time))
    #print time
        