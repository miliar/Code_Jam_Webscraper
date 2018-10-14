def time2int(timestr):
    """Converts time in the format specified by problem statement into integer
    equal to number of minutes since beginning of the day."""
    hours,minutes=map(int,timestr.split(":"))
    return hours*60 + minutes

def toggled(val):
    """Returns value from 0,1 not equal to val. val must be one of 0,1."""
    rets=[1,0]
    return rets[val]

def solve(turnaround, A2B, B2A):
    """Solves the problem for specified turnaround time, A2B contains list of
    lines, each specifying departure and arrival time as in problem statement,
    from A to B, B2A just like A2B, only the departure and arrival time is from
    B to A."""
    schedules_str=(A2B,B2A)
    schedules=[]
    for schedule_str in schedules_str:
        schedule=[]
        for item_str in schedule_str:
            item=map(time2int,item_str.split(" "))
            schedule.append(item)
        schedules.append(schedule)
    trains=[0,0]
    for station in (0,1):
        a=1
        departures=[dep for (dep,arr) in schedules[station]]
        arrivals=[arr for (dep,arr) in schedules[toggled(station)]]
        departures.sort()
        arrivals.sort()
        nArrivals=len(arrivals)
        nDepartures=len(departures)
        dep=0
        arr=0
        next_available_queue=[]
        while arr<nArrivals and dep<nDepartures:
            if departures[dep]<arrivals[arr]:
                if not next_available_queue or next_available_queue[0]>departures[dep]:
                    trains[station]+=1
                else:
                    next_available_queue.pop(0)
                dep+=1
            else:
                next_available_queue.append(arrivals[arr]+turnaround)
                arr+=1
        if arr<nArrivals:
            #arriving trains are OK
            pass
        else:
            #dep<nDepartures
            while dep<nDepartures:
                if not next_available_queue or next_available_queue[0]>departures[dep]:
                    trains[station]+=1
                else:
                    next_available_queue.pop(0)
                dep+=1
    return trains

if __name__=='__main__':
    import sys
    f=open(sys.argv[1],'rt')
    N=int(f.readline().rstrip())
    solutions=[]
    for n in range(N):
        turnaround=int(f.readline().rstrip())
        nA2B,nB2A=map(int, f.readline().rstrip().split(" "))
        A2B=[]
        B2A=[]
        for i in range(nA2B):
            A2B.append(f.readline().rstrip())
        for i in range(nB2A):
            B2A.append(f.readline().rstrip())
        solutions.append(solve(turnaround,A2B,B2A))
#    while line!="":
#        if turnaround==None:
#            turnaround=int(line)
#        elif nA2B==None:
#            nA2B,nB2A=map(int,line.split(' '))
#            A2B=[]
#            B2A=[]
#        else:
#
#            if nA2B>0:
#                A2B.append(line)
#                nA2B-=1
#            else: #nB2A must be >0
#                B2A.append(line)
#                nB2A-=1
#                if nB2A==0:
#                    solutions.append(solve(turnaround,A2B,B2A))
#                    nA2B=None
#                    turnaround=None
#        line=f.readline().rstrip()
    for (i,solution) in enumerate(solutions):
        print "Case #%(i)s: %(A)s %(B)s" % {
                'i': i+1,
                'A': solution[0],
                'B': solution[1],
                }
