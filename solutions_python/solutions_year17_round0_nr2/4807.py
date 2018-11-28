filenameInput = "B-small-attempt0.in"
#filenameInput = "test.in"
filenameOutput = "B-small-attempt0.out"

def tidyNumbers(S):
    if(len(S)==1):
        return S
    if(isSorted(S)):
        return S
    return tidyNumbers(str(int(S)-1))

def isSorted(number):
    num = list(number)
    for i in range(len(num)-1,0,-1):
        op = int(num[i]) - int(num[i-1])
        if (op >= 0):
            continue
        else:
            return False
    return True


def loadFile():
    f = open(filenameInput,"r")
    tc = int(f.readline())
    string=""
    i=1
    while(i<=tc):
        number = str(int(f.readline()))
        c = tidyNumbers(number)
        string += "Case #"+str(i)+": "+c+"\n" if i<tc else "Case #"+str(i)+": "+c
        i+=1
    saveFile(string)
    f.close()

def saveFile(string):
    f = open(filenameOutput,"w")
    #f.write("Case #",x,": ",y, )
    f.write(string)
    f.close()

loadFile()
