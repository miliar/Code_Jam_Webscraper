def convert(DepartList,ReadyList):
        DepartList.sort()
        ReadyList.sort()
        n=0
        for i in DepartList:
                n+=1                
                for j in ReadyList:
                        if j<=i:
                                n-=1
                                ReadyList.remove(j)
                                break
        return n

                
                
inputf=file('B-small.in')
outputf=file('B-small.out','w')
N=int(inputf.readline())
for k in range(N):
        TT=int(inputf.readline())
        [NA,NB]=[int(i) for i in inputf.readline().split()]
        if NA==0 or NB==0:
                outputf.write('Case #'+str(k+1)+': '+str(NA)+' '+str(NB)+'\n')
                continue
        Aarrival=[]
        Barrival=[]
        Adept=[]
        Bdept=[]
        for j in range(NA):
                [arrivals,depts]=inputf.readline().split()
                arrival=[int(i) for i in arrivals.split(':')]
                arrivalt=arrival[0]*60+arrival[1]
                dept=[int(i) for i in depts.split(':')]
                deptt=dept[0]*60+dept[1]+TT
                Adept.append(arrivalt)
                Barrival.append(deptt)
        for j in range(NB):
                [arrivals,depts]=inputf.readline().split()
                arrival=[int(i) for i in arrivals.split(':')]
                arrivalt=arrival[0]*60+arrival[1]
                dept=[int(i) for i in depts.split(':')]
                deptt=dept[0]*60+dept[1]+TT
                Bdept.append(arrivalt)
                Aarrival.append(deptt)
        m=convert(Adept[:],Aarrival[:])
        n=convert(Bdept[:],Barrival[:])
        outputf.write('Case #'+str(k+1)+': '+str(m)+' '+str(n)+'\n')
inputf.close()
outputf.close()
print 'finish'
    
