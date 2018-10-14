
f = open('A-small-attempt0.in', 'r')

T = int(f.readline().strip())

import math

def stackArea(scakes):

    area=0

    [Ri,Hi]=scakes[0]
    tarea=math.pi*Ri*Ri
    area+=tarea
    for i in xrange(0,len(scakes)):
        [Ri,Hi]=scakes[i]
        area+=2*math.pi*Ri*Hi
        area+=(math.pi*Ri*Ri)-tarea
        tarea=math.pi*Ri*Ri

    #print "area",area

    return area

def stack(rcakes,scakes,K):

    area=0
    if len(scakes)==K:
        area=stackArea(scakes)
        return area
    else:
        marea=0
        for cake in rcakes:
            rcakes_=rcakes[:]
            scakes_=scakes[:]
            scakes_.append(cake)
            rcakes_.remove(cake)
            area=stack(rcakes_,scakes_,K)
            if area>marea:
                marea=area
                #print area,marea
        return marea

for t in xrange(T):

    line = f.readline().strip()
    N=int(line.split(" ")[0])
    K=int(line.split(" ")[1])

    cakes=[]
    for i in xrange(N):
        line = f.readline().strip()
        Ri=float(line.split(" ")[0])
        Hi=float(line.split(" ")[1])
        cakes.append([Ri,Hi])    
    
    area=stack(cakes[:],[],K)

    print 'Case #%d: %f'% (t+1,area)