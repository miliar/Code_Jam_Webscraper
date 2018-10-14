

file1=open("input2.txt",'r')
file2=open("output.txt",'w')

def possible(numtosolve,surp,bestscore):
    if(bestscore==1):
        if(numtosolve>=1):
            return (surp,True)
        else:
            return (surp,False)
    if(bestscore==0):
        return (surp,True)
    
    if(numtosolve>=3*bestscore-2):
        return (surp,True)
    if(numtosolve<3*bestscore-4):
        return (surp,False)
    if(surp>0):
        surp=surp-1
        return (surp,True)
    else :
        return (surp,False)


numofcases=int(file1.readline())
for i in range (0,numofcases):
    tc=file1.readline()
    spltc=tc.split()
    best=0
    numofgooglers=int(spltc[0])
    surp=int(spltc[1])
    bestscore=int(spltc[2])
    for x in range(0,numofgooglers):
        numtosolve=int(spltc[x+3])
        arr=possible(numtosolve,surp,bestscore)
        if(arr[1]==True):
            surp=arr[0]
            best=best+1
    file2.write("Case #"+str(i+1)+": "+str(best)+"\n")
file2.close()                




