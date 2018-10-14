from collections import deque
fread = open("C-small-attempt0.in","r")
fout = open("C-small-attempt0.out","w")
lineCount=0
caseCount=0
testCaseNum=0
caseDescribe=False
caseGroup=False
for line in fread:
    lineCount+=1
    if lineCount==1:
        testCaseNum=line.strip()
        print "total Test Case:"+testCaseNum
    elif lineCount%2==0:
        caseDescribe=True
        caseGroup=False
        caseCount+=1
        (round, max, group)=line.split()
        round=int(round)
        max=int(max)
        group=int(group)
        print "case Describe=:"+str((round, max, group))
    elif lineCount%2==1:
        money=0
        caseGroup=True
        caseDescribe=False
        groupList=line.split()
        queue = deque(groupList)
        print "groupList="+str(groupList)
    
    if caseGroup==True:
        money=0
        tmpList=[]
        for rindex in range(0, int(round)):
            #add list back to queue
            for list in tmpList:
                queue.append(list)
            groupIndex=0
            tmpMax=max
            tmpList=[]
            while(len(queue)!=0 and tmpMax >= int(queue[groupIndex])):
                tmpMax-=int(queue[groupIndex])
                money+=int(queue[groupIndex])
                #queue.append(queue[0])
                tmpList.append(queue[0])
                queue.popleft()
                
        print money
        fout.write("Case #"+str(caseCount)+": "+str(money)+"\n")
    