


def readfiles():
    f=open("C:\\Users\Dhruv Singhal\Documents\Visual Studio 2013\junk\googleCodeJam1\googleCodeJam1\B-small-attempt1.in","r")
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
        final.append("case #"+str(k+1)+": "+str(lists[k]))        
        k+=1
    writefile(final)
def writefile(array):
    fo=open("C:\\Users\Dhruv Singhal\Documents\Visual Studio 2013\junk\googleCodeJam1\googleCodeJam1\TextFile1.txt","w+")
    for i in range(100):
        fo.write(array[i]+"\n")
def main():
    thearray= readfiles()
    totaltasks = thearray[0]
    x=0
    thearray.pop(0)
    totaltasks=int(totaltasks.strip("\n"))
    result=[]
    while x< totaltasks:
        data = thearray[x].split(' ')
        cookies=float(data[0])
        frequency=float(data[1])
        totalCookies=float(data[2].strip("\n"))
        totalrate=2
        totaltime=0
        #calcluate the time needed 
        while totalCookies/totalrate > totalCookies/(frequency+totalrate)+cookies/totalrate:
            totaltime+=cookies/totalrate
            totalrate=frequency+totalrate
        result.append(round(totaltime+totalCookies/totalrate,7))    
        x+=1
    printresult(result)


if __name__ =="__main__":
    main()
