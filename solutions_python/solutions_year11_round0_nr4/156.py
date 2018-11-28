def processcase(inlist):
    tmp = inlist[:]
    inlist.sort()
    print tmp
    print inlist
    count = 0
    index = 0
    while index < len(inlist):
        if inlist[index] == tmp[index]:
            count += 1
        index += 1
    expected = len(inlist) - count
    return str(expected)+".000000"
    



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
        fout.write("Case #"+str(i)+": "+processcase(dinlist)+'\n')
    finput.close()
    fout.close()


if __name__=="__main__":
    inputfilter("D-large.in")