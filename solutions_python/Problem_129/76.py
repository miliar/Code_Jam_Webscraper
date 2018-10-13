def cost(f, to, people):
    return people*(N*(to-f) - (to-f)*(to-f-1)/2)
MOD=1000002013
T= int (raw_input())
    
for test in range(1,T+1):
    N, M= map(int, (raw_input()).split())
    delta=[]
    actual_cost=0
    for stop in range(0,M):
        f, to, people = map(int, (raw_input()).split())
        actual_cost+=cost(f,to,people)
        actual_cost=actual_cost%MOD
        delta.append((f,people))
        delta.append((to, -people))
    delta.sort()
    stations=[delta[0][0]]
    entry=[delta[0][1]]
    for station, value in delta[1:]:
        if station!= stations[-1]:
            stations.append(station)
            entry.append(value)
        else:
            entry[-1]+=value
    #print zip(stations,entry)
    total_cost=0
    for i in range(0, len(stations)):
        j=i-1
        while  entry[i]<0:
            m=min(-entry[i],entry[j])
            entry[i]+=m
            entry[j]-=m
            total_cost+=cost(stations[j],stations[i],m)
            total_cost=total_cost%MOD

            #print stations[j],stations[i],m,total_cost
            j-=1


    actual_cost=(actual_cost+MOD)%MOD
    total_cost=(total_cost+MOD)%MOD
    diff= actual_cost-total_cost
    diff=(diff+MOD)%MOD
        
    print "Case #{0}: {1}".format(test,diff)
    
