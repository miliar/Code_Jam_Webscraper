def cal(time, capacity, data):
    if sum(data)<=capacity:
        return sum(data)*time    
    table=[] #from start
    tablesum=[] #this time people
    data2=data*2
    np=len(data)
    start=0
    peoplein=0
    for i in xrange(1,time+1):
        if start in table:
            loopstart=table.index(start)
            #print table
            #print tablesum
            res=sum(tablesum)
            time=time-len(tablesum)
            tablesum=tablesum[loopstart:]
            return res+time/len(tablesum)*sum(tablesum)+\
                sum(tablesum[:time%len(tablesum)])
        else:
            peoplein=0
            table.append(start)
            for k in xrange(start, start+len(data)):
                peoplein+=data2[k]
                if peoplein+data2[k+1]>capacity:
                    tablesum.append(peoplein)
                    start=(k+1)%np
                    break
    return sum(tablesum)
    
nc=input()
for n in xrange(nc):
    time, capacity, ndata=[int(t) for t in raw_input().split()]
    data=[int(t) for t in raw_input().split()]
    data=data[0:ndata]
    res=cal(time, capacity, data)
    print "Case #%d: %d" % (n+1, res)




