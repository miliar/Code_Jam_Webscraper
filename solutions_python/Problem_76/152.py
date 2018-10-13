def processcase(inlist):
    inlist.sort()
    binarylist = []
    maxval = int(inlist[-1])
    length = len(tobinary(maxval,0))
    for i in inlist:
        binarylist.append(tobinary(int(i),length))
    if ispossible(binarylist,length):
        return spliter(inlist)
    else:
        return "NO"
    
def spliter(inlist):
    listsum = 0
    Pat = int(inlist[0])
    for i in inlist:
        listsum += int(i)
    Sean = listsum - Pat
    return Sean


def ispossible(binarylist, length):
    possible = True
    count = 0
    for i in range(0, length):
        for bstr in binarylist:
            count += int(bstr[i])
        if count%2 != 0:
            possible = False
            return possible
    return possible

def tobinary(n, length):
    bstr = ''
    if n == 0: return '0'
    while n > 0:
        bstr = str(n % 2) + bstr
        n = n >> 1
    while len(bstr)<length and length != 0:
        bstr = '0'+bstr
    return bstr

def inputfilter(filename):
    finput = open(filename,'r')
    fout = open("out.txt",'w')
    casenum = int(finput.readline())
    for i in range(1,casenum+1):
        length = int(finput.readline())
        dinlist = []
        inlist = finput.readline().split()
        for j in inlist:
            dinlist.append(int(j))
        fout.write("Case #"+str(i)+": "+str(processcase(dinlist))+'\n')
        print "Case #"+str(i)+": "+str(processcase(dinlist))+'\n'
    finput.close()
    fout.close()


if __name__=="__main__":
    inputfilter("C-large.in")