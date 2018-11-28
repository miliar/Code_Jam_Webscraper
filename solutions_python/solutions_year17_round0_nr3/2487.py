s = open('csmall.in')
sw = open('ctx.txt', 'w')

num = int(s.readline())
c = 1
while c <= num:
    numl = list(s.readline().split())
    stalls = int(numl[0])
    people = int(numl[1])
    rrs = 0
    rls=0
    if stalls == people:
        sw.write('Case #' + str(c) + ": " + "0 0")
        sw.write('\n')
    elif people ==1:
        sw.write('Case #' + str(c) + ": " + str(stalls//2) + " " + str((stalls-1)//2))
        sw.write('\n')
    else:
        dummy = [1]
        for x in range(stalls):
            dummy.append(0)
        dummy.append(1)


        chosen=0
        while(chosen<people):
            minlist = []
            maxlist = []
            minx = -10000
            maxx = -10000
            for x in range(1,len(dummy)-1):
                if dummy[x] ==0:
                    rs = 0
                    ls = 0
                    for i in range(x+1,len(dummy)):
                        if dummy[i]==1:
                            break
                        rs += 1
                    for p in range(x-1,-1,-1):
                        if dummy[p]==1:
                            break
                        ls+=1
                    if min(rs,ls)==minx:
                        minlist.append((x,ls,rs))
                    if min(rs,ls)>minx:
                        minlist = []
                        minlist.append((x,ls,rs))
                        minx = min(rs,ls)
                    if max(rs,ls)==maxx:
                        maxlist.append((x,ls,rs))
                    if max(rs,ls)>maxx:
                        maxlist = []
                        maxlist.append((x,ls,rs))
                        maxx=max(rs,ls)
            if len(minlist)==1:
                dummy[minlist[0][0]]=1
                rrs = minlist[0][2]
                rls = minlist[0][1]
            else:
                maxm=-1
                smaxlist = []
                for i in range(len(minlist)):
                    if max(minlist[i][2],minlist[i][1])==maxm:
                        smaxlist.append(minlist[i])
                    if max(minlist[i][2],minlist[i][1])>maxm:
                        maxm=max(minlist[i][2],minlist[i][1])
                        smaxlist=[]
                        smaxlist.append(minlist[i])
                dummy[smaxlist[0][0]]=1
                rls = smaxlist[0][1]
                rrs = smaxlist[0][2]



            chosen+=1
        sw.write('Case #' + str(c) + ": " + str(max(rls,rrs)) + " " + str(min(rls,rrs)))
        sw.write('\n')
    c+=1