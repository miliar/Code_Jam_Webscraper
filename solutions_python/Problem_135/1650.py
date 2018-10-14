


def readfiles():
    f=open("C:\\Users\Dhruv Singhal\Documents\Visual Studio 2013\junk\googleCodeJam1\googleCodeJam1\A-small-attempt1.in","r")
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
        if len(lists[k])==1:
            final.append("case #"+str(k+1)+": "+str(lists[k].pop()))
        elif len(lists[k])>1 :
            final.append("case #"+str(k+1)+": "+"Bad magician!")
        elif len(lists[k])==0:
            final.append("case #"+str(k+1)+": "+"Volunteer cheated!")
        k+=1
    writefile(final)
def writefile(array):
    fo=open("C:\\Users\Dhruv Singhal\Documents\Visual Studio 2013\junk\googleCodeJam1\googleCodeJam1\TextFile1.txt","w+")
    for i in range(100):
        fo.write(array[i]+"\n")
def main():
    thearray= readfiles()
    totaltasks = thearray[0]
    x=1
    thearray.pop(0)
    totaltasks=int(totaltasks.strip("\n"))
    result=[]
    while x<= totaltasks:
        row1= thearray[0].strip("\n")
        row2=thearray[5].strip("\n")
        result.append(set(thearray[int(row1)].split()) & set(thearray[int(row2)+5].split()))
        y=0
        while y<=9:
            thearray.pop(0)
            y+=1
        x+=1
    printresult(result)


if __name__ =="__main__":
    main()
