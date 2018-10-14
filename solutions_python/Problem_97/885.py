myFile = open("C-small-attempt0.in", "r")
inputlist = list()
for myLine in myFile:
    if not inputlist:
        inputlist.append(int(myLine))
    else:
        li = myLine.split()
        inputlist.append((int(li[0]),int(li[1])))

def rotatenum(x,places):
    s = str(x)
    return int(s[places:] + s[0:places])


outputFile = open('recycle.out','w')
for casenum,(a,b) in enumerate(inputlist[1:]):
    memo = set()
    result = set()
    for n in xrange(a,b+1):
        ms = sorted([rotatenum(n,r) for r in xrange(len(str(n)))])
        if ms[0] not in memo:
            for i in xrange(len(ms)-1):
                for j in xrange(i+1,len(ms)):
                    if a <= ms[i] < ms[j] <= b:
                        result.add((ms[i],ms[j]))
            memo.add(ms[0])
    outputFile.write('Case #'+str(casenum+1)+': '+str(len(result))+'\n')

outputFile.close()

