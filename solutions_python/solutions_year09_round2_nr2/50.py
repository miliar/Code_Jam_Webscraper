iFileName = 'B-large.in'
oFileName = 'output'


def genNextNum(numStr):
    l = len(numStr)
    pos = l-1
    while pos>0:
        if numStr[pos-1]<numStr[pos]:
            break
        pos-=1
    if pos ==0:
        numStr='0'+numStr
        l +=1
    else:
        pos-=1
    tPos = pos
    tNum = numStr[tPos]
    tPos+=1
    while tPos<l and numStr[tPos]>tNum:
        tPos+=1
    tPos-=1
    #print('pos:',pos,',tPos:',tPos,'num:',numStr)
    nxtNum = ''
    if pos>0:
        nxtNum = numStr[:pos]
    nxtNum +=numStr[tPos]
    if tPos<l-1:
        nxtNum += numStr[:tPos:-1]
    nxtNum += numStr[pos]
    if tPos-pos>1:
        nxtNum += numStr[tPos-1:pos:-1]
    return nxtNum
        
    
def nextNum():
    iFile = open(iFileName)
    oFile= open(oFileName,'w')
    line = iFile.readline()
    caseCnt = int(line)
    for caseNo in range(caseCnt):
        numStr = iFile.readline().strip()
        oFile.write('Case #%d: %s\n' %(caseNo+1,genNextNum(numStr)))
    iFile.close()
    oFile.close()
'''
while True:
    n = input('num:').strip()
    print(genNextNum(n))
    '''

nextNum()
print("DONE")
