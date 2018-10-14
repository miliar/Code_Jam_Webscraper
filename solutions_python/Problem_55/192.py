def read():
    nRun,limit,nGroup = map(int,raw_input().split())
    group = map(int,raw_input().split())
    return nRun,limit,group


def stepRun(limit,idx,group):
    moved = 0
    earned = 0
    remain = limit

    for j in range(len(group)):
        if remain-group[idx]<0:
            break;
        earned += group[idx]
        remain -= group[idx]
        moved += 1
        idx = (idx+1)%len(group)

    return moved,earned


def work(cases,(nRun,limit,group)):
    tbl = [(-1,-1) for i in range(len(group))] # tbl[idx] = (earned,run)

    earned = 0
    idx = 0

    for i in range(nRun):
        tbl[idx] = (earned,i)
        
        stepMoved,stepEarn = stepRun(limit,idx,group)
        idx = (idx+stepMoved)%len(group)
        earned += stepEarn
        
        if tbl[idx]!=(-1,-1):
            cycleLen = i+1-tbl[idx][1]
            cycleEarn = earned-tbl[idx][0]
            earned += (nRun-i-1)/cycleLen*cycleEarn
            
            for j in range((nRun-i-1)%cycleLen):
                stepMoved,stepEarn = stepRun(limit,idx,group)
                idx = (idx+stepMoved)%len(group)
                earned += stepEarn
            break
    
    print "Case #%d: %d"%(cases,earned)
        
        
for i in range(int(raw_input())):
    work(i+1,read())
