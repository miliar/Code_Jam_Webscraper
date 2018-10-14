iFileName = 'A-large.in'
oFileName = 'output'

#dTree = {'w':0,'f':None,'l':None,'r':None} # w,f,l,r

def readTree(treeStr):
    treeStr = treeStr.strip()
    treeStr = treeStr[1:-1].strip()
    tArr = treeStr.split(' ',2)
    #print(tArr)
    w = float(tArr[0])
    if len(tArr)==1:
        f= None
        tl = None
        tr = None
    else:
        f = tArr[1]
        sTreeStr = tArr[2]
        khCnt = 0
        pos = 0
        for ch in sTreeStr:
            pos+=1
            if ch=='(':
                khCnt +=1
            elif ch==')':
                khCnt -=1
            if khCnt == 0:
                break
        tlStr = sTreeStr[0:pos]
        trStr = sTreeStr[pos:]
        #print('l:',tlStr,',r:',trStr)
        tl = readTree(tlStr)
        tr = readTree(trStr)
    return {'w':w,'f':f,'l':tl,'r':tr}
    
def initTree(treeStr):
    return readTree(treeStr)

def prob(animalStr,dTree):
    tArr = animalStr.split(' ')
    features = tArr[2:] if len(tArr)>2 else []
    #print (features)
    tree = dTree
    p = 1.0
    while True:
        #print (tree['w'])
        p *= tree['w']
        fName = tree['f']
        if not fName:
            break # leaf
        #print(fName,":",features.count(fName))
        if features.count(fName)>0:
            tree = tree['l']
        else:
            tree = tree['r']
    return p

        
def decision():
    iFile = open(iFileName)
    oFile= open(oFileName,'w')
    line = iFile.readline()
    caseCnt = int(line)
    for caseNo in range(caseCnt):
        oFile.write('Case #'+str(caseNo+1)+':\n')
        # read tree
        lineCnt = int(iFile.readline())
        treeStr = ""
        for treeLineNo in range(lineCnt):
            treeStr+=" "+iFile.readline().strip()
        dTree = initTree(treeStr)
        #print(dTree)
        animalCnt = int(iFile.readline())
        for animalNo in range(animalCnt):
            oFile.write("%.7f\n" % prob(iFile.readline().strip(),dTree))    
    iFile.close()
    oFile.close()
                        
decision()
print("DONE")
