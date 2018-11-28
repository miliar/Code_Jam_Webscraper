def checkLightState(numSnappers, numClicks):
    if numClicks==0:
        return False
    target=pow(2, numSnappers)-1
    if numClicks<target:
        return False
    if numClicks==target:
        return True
    difference=numClicks-target
    if difference<(target+1):
        return False
    if difference==(target+1):
        return True
    remainder=difference%(target+1)
    if remainder==0:
        return True
    else:
        return False
    

def ASmall():
    fIn=open('A-large.in.txt', 'r')
    fOut=open('A-Large.out', 'w')
    first=True
    caseNum=0
    for line in fIn:
        if first:
            first=False
            numCases=int(line)
            print 'num of cases=', numCases
        else:
            caseNum=caseNum+1
            parts=line.rsplit(' ')
            numSnappers=int(parts[0])
            numClicks=int(parts[1])
            isOn=checkLightState(numSnappers, numClicks)
            fOut.write('Case #')
            fOut.write(str(caseNum))
            fOut.write(': ')
            if isOn:
                fOut.write('ON\n')
            else:
                fOut.write('OFF\n')
    fIn.close()
    fOut.close()
                


if __name__=="__main__":
    ASmall()
