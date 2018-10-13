f=open('F:\\tah.txt')
test=int(f.readline())
for i in range(test):
    line=[]
    olist=[]
    blist=[]
    olistpos=0
    blistpos=0
    opos=1
    bpos=1
    time=0
    line=f.readline().split()
    while(len(line)<(int(line[0])*2 + 1)):
        line.extend(f.readline().split())
    for j in range(1,(int(line[0])*2),2):
        if(line[j]=='O'):
            olist.append(j+1)
        else:
            blist.append(j+1)
    for j in range(1,(int(line[0])*2),2):
        if(line[j]=='O'):
            olistpos+=1
            newtime=abs(int(line[j+1])-opos)+1
            time+=newtime
            opos=int(line[j+1])
            if(blistpos<len(blist)):
                bnextpos=int(line[blist[blistpos]])
                if(bpos!=bnextpos):
                    if(bpos<bnextpos):
                        if((bnextpos-bpos)<=newtime):
                            bpos=bnextpos
                        else:
                            bpos+=newtime
                    else:
                        if((bpos-bnextpos)<=newtime):
                            bpos=bnextpos
                        else:
                            bpos-=newtime
        else:
            blistpos+=1
            newtime=abs(int(line[j+1])-bpos)+1
            time+=newtime
            bpos=int(line[j+1])
            if(olistpos<len(olist)):
                onextpos=int(line[olist[olistpos]])
                if(opos!=onextpos):
                    if(opos<onextpos):
                        if((onextpos-opos)<=newtime):
                            opos=onextpos
                        else:
                            opos+=newtime
                    else:
                        if((opos-onextpos)<=newtime):
                            opos=onextpos
                        else:
                            opos-=newtime
    print "Case #{0}: {1}".format(i+1,time)
