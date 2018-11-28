


f = open(r'C:\Ggl\qual\B-large.in')

numcases=int(f.readline())
for case in range(numcases):
    line=f.readline().strip()
    turnaround=int(line)
    
    line=f.readline().strip()
    (na, nb) = map(int, line.split(' '))
    
    depA=[]
    depB=[]
    arrA=[]
    arrB=[]
    
    for a in range(na):
        line=f.readline().strip()
        (time1, time2) = line.split(' ')
        (h1, m1) = time1.split(':')
        (h2, m2) = time2.split(':')
        depA.append(int(h1)*60+int(m1))
        arrB.append(int(h2)*60+int(m2)+turnaround)
    
    for b in range(nb):
        line=f.readline().strip()
        (time1, time2) = line.split(' ')
        (h1, m1) = time1.split(':')
        (h2, m2) = time2.split(':')
        depB.append(int(h1)*60+int(m1))
        arrA.append(int(h2)*60+int(m2)+turnaround)

    trainsA=0
    for dep in depA:
        usetrain = -1
        for arr in arrA:
            if arr <= dep and (arr > usetrain or usetrain == -1):
                usetrain = arr
                
        if usetrain != -1:
            arrA.remove(usetrain)
        else:
            trainsA += 1
        
    trainsB=0
    for dep in depB:
        usetrain = -1
        for arr in arrB:
            if arr <= dep and (arr > usetrain or usetrain == -1):
                usetrain = arr

        if usetrain != -1:
            arrB.remove(usetrain)
        else:
            trainsB += 1


    print "Case #" + str(case+1) + ": " + str(trainsA) + ' ' + str(trainsB)


        






