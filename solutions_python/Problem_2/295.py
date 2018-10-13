class train: pass

def GetData(counta, countb):
    global ifile

    entries=[]

    for i in range(counta):
        l=ifile.readline()
        print l
        l=l.replace('\n','')
        l=l.split(' ')

        start=l[0]
        end=l[1]
        origin='A'
        train=-1
        nextdeparture='??:??'

        s=[start,end,train,origin,nextdeparture]
        
        entries.append(s)

    for i in range(countb):
        l=ifile.readline()
        print l
        l=l.replace('\n','')
        l=l.split(' ')

        start=l[0]
        end=l[1]
        origin='B'
        train=-1
        nextdeparture='??:??'

        s=[start,end,train,origin,nextdeparture]
        
        entries.append(s)


    entries.sort()

    return entries

def Best(travels, turnaround):

    parkedA=[]
    parkedB=[]
    trainsA=0
    trainsB=0

    for travel in travels:
        start=travel[0]
        end=travel[1]
        origin=travel[3]
        if origin=='A':
            parked=parkedA
            parking=parkedB
            target='B'
        else:
            parked=parkedB
            parking=parkedA
            target='A'

        print >> odebug, 'travel ', travel

        print >> odebug, 'parked on A'
        for pp in  parkedA:
            print >> odebug, pp

        print >> odebug, 'parked on B'
        for pp in  parkedB:
            print >> odebug, pp

        if len(parked)==0: #need a new train
            newTrain=1
        elif parked[0][0] > start:  #need a new train
            newTrain=1            
        else: #use the train parked
            newTrain=0
            #using a train is just removing it for the top
            currentTrain=parked[0][1]
            parked.pop(0)
            

        if newTrain==1:
            if origin=='A':
                trainsA=trainsA+1
                currentTrain='A%03i' % trainsA
            else:
                trainsB=trainsB+1
                currentTrain='B%03i' % trainsB
                
        travel[2]=currentTrain

        #calculate next departure

        minutes=int(end[3:]) + turnaround
        hour=int(end[0:2])

        if minutes>60:
            minutes=minutes-60
            hour=hour+1

        nextdeparture='%02i:%02i' % (hour,minutes)
        travel[4]=nextdeparture
        #park the train at othe side

        
        parking.append([nextdeparture,currentTrain])
        parking.sort()

    return trainsA, trainsB
            


ifile=file("B-large.in.txt","r")
ofile=file("saida.txt","w")
odebug=file("debug.txt","w")

casos=int(ifile.readline())


for caso in range(casos):
    turnaround = int(ifile.readline())
    
    l=ifile.readline().split()
    ab_count=int(l[0])
    ba_count=int(l[1])
    
    travels=GetData(ab_count, ba_count)

    


    best=Best(travels, turnaround)


    saida="Case #%i: %i %i\n" % (caso+1,best[0],best[1])
    print >> odebug, turnaround
    print >> odebug, saida
    ofile.write(saida)

    
ifile.close()
ofile.close()
odebug.close()
