def unsurprising(score,best):
    return score >= best + max(0,best-1) + max(0,best-1)

def surprising(score,best):
    return score >= best + max(0,best-2) + max(0,best-2) and not unsurprising(score,best)

inputlist = list()
myFile = open("B-large.in", "r")
for myLine in myFile:
    if not inputlist:
        inputlist.append(int(myLine))
    else:
        li = myLine.split()
        inputlist.append([int(x) for x in li])
myFile.close()

outputFile = open('dancing-googlers-large.out','w')
for casenum,li in enumerate(inputlist[1:]):
    [N,S,p] = li[:3]
    result = sum(unsurprising(score,p) for score in li[3:]) + min(S,sum(surprising(score,p) for score in li[3:]))
    outputFile.write('Case #'+str(casenum+1)+': '+str(result)+'\n')
    outputFile.flush()

outputFile.close()
