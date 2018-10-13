#!/usr/bin/python2


def outPut(ansSeq,filename='out'):

    outFile = open(filename,'w')
    outFile.writelines(ansSeq)
    outFile.close()
    return None

def str2list(inputstr):
    return [int(i) for i in inputstr[2:].strip()]

def numInvite(case):
    invite = 0
    level = 0
    stand = 0
    tmpinvite = 0
    for i in case:
        if i > 0:
            if stand < level :
                tmpinvite = level - stand
                invite += level - stand
            stand += tmpinvite + i
        level += 1
    return invite


def solve(filename='A-small-attempt2.in'):
    ans = []
    inFile = open(filename,'r',0)
    tot = int(inFile.readline().strip())
    numcase = 1
    for i in range(tot):
        invite = numInvite(str2list(inFile.readline()))
        output = 'Case #'+str(numcase)+': '+str(invite)
        ans.append(output+'\n')
        print output
        numcase += 1
    inFile.close()
    return ans

def writeFile():
    outPut(solve())
    
    


        
