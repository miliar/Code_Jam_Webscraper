for tc in xrange(int(raw_input())):
    dist,walk,run,energy,numofwalkways=map(float,raw_input().split())
    walkways=[]
    walkwaydist=0
    for i in xrange(int(numofwalkways)):
        meh=map(int,raw_input().split())
        meh=[meh[2]]+meh[0:2]
        walkways.append(meh)
        walkwaydist+=meh[2]-meh[1]
    walkways.append([0,0,dist-walkwaydist])
    walkways.sort()
    #print walkways
    totaltime=0.0
    totaldist=0.0
    for i in walkways:
        if energy>(i[2]-i[1])/(run+i[0]):
            totaltime+=(i[2]-i[1])/(run+i[0])
            totaldist+=i[2]-i[1]
            energy-=(i[2]-i[1])/(run+i[0])
        elif energy>0:
            totaltime+=energy
            totaltime+=(i[2]-i[1]-energy*(run+i[0]))/(i[0]+walk)
            totaldist+=i[2]-i[1]
            energy=0
        else:
            totaltime+=(i[2]-i[1])/(i[0]+walk)
            totaldist+=(i[2]-i[1])
    print "Case #"+str(tc+1)+":",totaltime
