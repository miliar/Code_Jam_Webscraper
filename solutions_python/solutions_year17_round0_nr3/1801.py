inputval=int(input())
outputlist=[None]*inputval
for i in range(0,inputval):
    inpvalue=input()
    temporary=inpvalue.split()
    temp1=int(temporary[0])
    temp2=int(temporary[1])
    count=0
    templist=[temp1]
    result=[None,None]
    while(count!=temp2):
        temp1=max(templist)
        if(temp1%2!=0):
            temp=temp1//2
            result=[temp,temp]
            templist[templist.index(temp1)]=temp
            templist.append(temp)
        else:    
            temp=temp1//2
            result=[temp,temp-1]
            templist[templist.index(temp1)]=temp
            templist.append(temp-1)
        count=count+1
    outputlist[i]=result
for n in range(len(outputlist)):
    outputvalue="Case #"+str((n+1))
    outputvalue=str(outputvalue)+": "+str(outputlist[n][0])+" "+str(outputlist[n][1])
    print(outputvalue)
