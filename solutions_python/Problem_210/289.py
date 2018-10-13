import sys
import math


def dist(start,end):
    if end>=start: 
        return end-start
    return (1440-start) + end



fin = sys.stdin
fout = sys.stdout
ferr = sys.stderr

T = int(fin.readline())

for case in range(T):
    l = fin.readline()
    AC = int(l.split()[0])
    AJ = int(l.split()[1])

    pans = []
    for i in range(AC):
        l = fin.readline()
        S = int(l.split()[0])
        K = int(l.split()[1])        
        pans.append( (S, K, 'C') )

    for i in range(AJ):
        l = fin.readline()
        S = int(l.split()[0])
        K = int(l.split()[1])        
        pans.append( (S, K, 'J') )
    
    ##############################

    pans = sorted(pans)
    Csum = 0
    Jsum = 0
    Free = 0
    C = []
    J = []
    switches = 0
    for i in range(len(pans)):
        j = (i+1)%len(pans)
        S1,K1,O1 = pans[i]
        S2,K2,O2 = pans[j]

        if O1=='C': Csum += K1-S1
        else:       Jsum += K1-S1

        gap = dist(K1,S2)
        if O1!=O2:      
            Free += gap
            switches += 1
        elif O1=='C':   C.append(gap)
        else:           J.append(gap)

    C = sorted(C, reverse=True)
    J = sorted(J, reverse=True)
    sumC = sum(C)
    sumJ = sum(J)
    
    if sumC+Csum+Free>=720 and sumJ+Jsum+Free>=720: 
        fout.write("Case #%i: %i\n" % (case+1, switches))
        continue

    if sumC+Csum+Free < sumJ+Jsum+Free: 
        for j in J:
            sumC += j
            switches += 2
            if sumC+Csum+Free>=720:
                break        
    else:
        for c in C:
            sumJ += c
            switches += 2     
            if sumJ+Jsum+Free>=720:
                break   

    fout.write("Case #%i: %i\n" % (case+1, switches))







