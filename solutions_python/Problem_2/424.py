from sets import Set
import sys

file=open(sys.argv[1],'r')
lines=file.readlines()
file.close()

count=0
N=int(lines[count])
count+=1

for i in range(0,N):
    T=int(lines[count])
    count+=1

    tstring=lines[count].rstrip().split(' ')
    NA=int(tstring[0])
    NB=int(tstring[1])
    count+=1

    atimes=[]
    for j in range(0,NA):
        ttime=lines[count].rstrip().split(' ')
        count+=1
        stime=ttime[0].split(':')
        s=60*int(stime[0])+int(stime[1])
        etime=ttime[1].split(':')
        e=60*int(etime[0])+int(etime[1])+T
        t=(s,e)
        atimes.append(t)

    btimes=[]
    for j in range(0,NB):
        ttime=lines[count].rstrip().split(' ')
        count+=1
        stime=ttime[0].split(':')
        s=60*int(stime[0])+int(stime[1])
        etime=ttime[1].split(':')
        e=60*int(etime[0])+int(etime[1])+T
        t=(s,e)
        btimes.append(t)

    sames=Set()
    taken=[]
    for pq in range(0,len(btimes)):
        taken.append(0)
    for m in range(0,len(atimes)):
        mindiff=100000
        index=-1
        for n in range(0,len(btimes)):
            atrain=atimes[m]
            btrain=btimes[n]
            diff=btrain[0]-atrain[1]
            if diff < mindiff and diff >= 0 and taken[n] == 0:
                mindiff=diff
                index=n
        if index > -1:
            tset=Set()
            tset.add(m)
            tset.add(index+len(atimes)+len(btimes))
            taken[index]=1
            sames.add(tset)
        else:
            tset=Set()
            tset.add(m)
            sames.add(tset)

    taken=[]
    for pq in range(0,len(atimes)):
        taken.append(0)
    for m in range(0,len(btimes)):
        mindiff=100000
        index=-1
        for n in range(0,len(atimes)):
            atrain=atimes[n]
            btrain=btimes[m]
            diff=atrain[0]-btrain[1]
            if diff < mindiff and diff >= 0 and taken[n]==0:
                mindiff=diff
                index=n
        if index > -1:
            tset=Set()
            tset.add(m+len(atimes)+len(btimes))
            tset.add(index)
            taken[index]=1
            sames.add(tset)
        else:
            tset=Set()
            tset.add(m+len(atimes)+len(btimes))
            sames.add(tset)

    flag=True
    while flag:
        msames=Set()
        for s in sames:
            mycount=0
            for t in sames:
                if s==t:
                    continue
                if len(s & t) > 0:
                    mycount+=1
                    temps=s|t
                    msames.add(temps)
            if mycount==0:
                msames.add(s)
        if len(sames) == len(msames):
            flag=False
        sames=msames.copy()

    acount=0
    bcount=0
    for s in sames:
        minstart=100000
        winner=-1
        for t in s:
            if t < len(atimes)+len(btimes):
                st=atimes[t]
                stime=st[0]
                if stime<minstart:
                    minstart=stime
                    winner=0
            else:
                st=btimes[t-len(atimes)-len(btimes)]
                stime=st[0]
                if stime<minstart:
                    minstart=stime
                    winner=1
        if winner==0:
            acount+=1
        else:
            bcount+=1
    print 'Case #'+str(i+1)+': '+str(acount)+' '+str(bcount)
