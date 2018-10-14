def centralize(QueryList,ServerList,Q,S):
        index1=[]
        if(S>Q):
            return 0
        switches=0
        while len(QueryList)!=1:
                index1=[]
                for i in ServerList:
                        j=-1
                        try:
                                j=QueryList.index(i)
                        except:
                                pass
                                           
                        index1.append(j)
                                          
                try:
                        index1.index(-1)
                        return switches
                except:
                        pass
                QueryList=QueryList[max(index1):]
                switches+=1
        return switches

inputf=file('A-large.in')
outputf=file('A-large.out','w')
N=int(inputf.readline())
for i in range(N):
    S=int(inputf.readline())
    ServerList=[]
    for j in range(S):
        ServerList.append(inputf.readline().split('\n')[0])
    Q=int(inputf.readline())
    QueryList=[]
    for k in range(Q):
        QueryList.append(inputf.readline().split('\n')[0])
    outputf.write('Case #'+str(i+1)+': '+str(centralize(QueryList,ServerList,Q,S))+'\n')
inputf.close()
outputf.close()
print 'finish'
    
