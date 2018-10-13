


def readfiles():
    f=open("C:\\Users\Dhruv Singhal\Documents\Visual Studio 2013\junk\googleCodeJam1\googleCodeJam1\D-large.in","r")
    contents=[]
    fl= f.readlines()
    for x in fl:
        contents.append(x)
    f.close()
    return contents

# program starts here --
def printresult(result):
    lists = list(result)
    k=0
    final=[]
    while k< len(lists):
        final.append("case #"+str(k+1)+": "+str(lists[k][0])+" "+str(lists[k][1]))        
        k+=1
    writefile(final)
def writefile(array):
    fo=open("C:\\Users\Dhruv Singhal\Documents\Visual Studio 2013\junk\googleCodeJam1\googleCodeJam1\TextFile1.txt","w+")
    for i in range(len(array)):
        fo.write(array[i]+"\n")
def main():
    thearray= readfiles()
    totaltasks = thearray[0]
    x=0
    thearray.pop(0)
    totaltasks=int(totaltasks.strip("\n"))
    result=[]
    new=[]
    while x< totaltasks:
        totalcases= int(thearray[0].strip("\n"))
        naomicollection = thearray[1].split(' ')
        naomicollection[len(naomicollection)-1]=naomicollection[len(naomicollection)-1].strip("\n")
        naomicollection=mapper(naomicollection)

        kencollection=thearray[2].split(' ')
        kencollection[len(kencollection)-1]=kencollection[len(kencollection)-1].strip("\n")
        kencollection=mapper(kencollection)
        storedkencollection=[]
        for ifg in range(len(kencollection)):
            storedkencollection.append(kencollection[ifg])
        storednaomicollection=[]
        for ifh in range(len(naomicollection)):
            storednaomicollection.append(naomicollection[ifh])
        kencollection.sort()
        kenmoves=[]
        returnValue=-2
        while len(naomicollection)>0:
            returnedValue=returnfirstlargest(naomicollection[0],kencollection)
            if returnedValue !=-1:
                kencollection.pop(kencollection.index(returnedValue))
            kenmoves.append(returnedValue)
            naomicollection.pop(0)
        ##d-war
        kencollection= storedkencollection
        naomicollection=storednaomicollection
        naomicollection.sort(reverse=True)
        kencollection.sort(reverse=True)
        totalnaomi=0
        while len(naomicollection)>0 and naomicollection[0] < kencollection[0]:
            naomicollection.pop(len(naomicollection)-1)
            kencollection.pop(0)
        kencollection.sort(reverse=False)
        naomimoves=[]
        returnedValue=0
        naomicollection.sort(reverse=False)
        while len(naomicollection)>0:
            variabl= kencollection.pop(0)
            returnedValue=returnfirstlargest(variabl,naomicollection)
            
            if returnedValue !=-1:
                naomicollection.pop(naomicollection.index(returnedValue))
                totalnaomi+=1
            else :
                naomicollection.pop(0)
                
        result.append(kenmoves)
        newresult=[]
        newresult.append(totalnaomi)
        
        newresult.append(result[len(result)-1].count(-1))
        
        new.append(newresult)
        for y in range(3):
            thearray.pop(0)
        x+=1
    printresult(new)
def returnfirstlargest(arg,list):
    newlist=[]
    for i in range(len(list)):
        newlist.append(list[i])
    while arg>newlist[0]:
        newlist.pop(0)
        if len(newlist)==0:
            return -1
    return newlist[0]
def mapper(array):
    return [float(i) for i in array]

if __name__ =="__main__":
    main()
