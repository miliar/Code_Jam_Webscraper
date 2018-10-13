 

def findVal(N,div,caseno):
    centerIndex=[]
    lst=[]
    lst.append(-1)
    lst.append(N)
    while(div>len(centerIndex)):
        tmp=[]
        tmp1=[]
        a=lst[:len(lst)-1]
        b=lst[1:]
        #print(a,b)
        ind1=0
        for i in range(len(a)):
            center=b[i]-a[i]
            if(center%2==0):
                center=center/2
            else:
                center=(center-1)/2
            lst.insert(ind1+1,a[i]+center)
            ind1+=2
            tmp.append(a[i]+center)
            tmp1.append(b[i]-a[i]-1)
            
        while(len(tmp1)>0):
            if max(tmp1)==-1:
                break
            index=tmp1.index(max(tmp1))
            centerIndex.append(tmp[index])
            tmp1[index]=-1
            if(div<len(centerIndex)): #reduce time
                break

    #print(centerIndex)
    lastPerson=centerIndex[div-1]
    centerIndex.sort()
    cuInd=centerIndex.index(lastPerson)
    if cuInd>0:
        Ls=centerIndex[cuInd]-centerIndex[cuInd-1]-1
    else:
        Ls=centerIndex[cuInd]
    if cuInd<len(centerIndex)-1:
        Rs=centerIndex[cuInd+1]-centerIndex[cuInd]-1
    else:
        Rs=N-centerIndex[cuInd]-1
    vall="Case #"+str(caseno+1)+": "+str(int(max(Ls,Rs)))+" "+str(int(min(Ls,Rs)))
    print(vall)
    writeFiles(vall)
            
def writeFiles(towrite):
    f.write(towrite+'\n')
    
def runWork(line,caseno):
    N=int(line.strip().split(" ")[0])
    K=int(line.strip().split(" ")[1])

    findVal(N,K,caseno)

                                                         
def openFiles(filename):
    with open(filename) as f:
        i=0
        for line in f:
            if(i>0):
                runWork(line,i-1)
            i+=1

global f
f = open('C-small-1-attempt0.out', 'w')
openFiles('C-small-1-attempt0.in')
f.close()
