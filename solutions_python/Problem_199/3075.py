InputFilename='A-large.in'
OutputFilname=InputFilename.replace("in","out")
#print OutputFilname
inpFile = open(InputFilename, 'r')
outFile = open(OutputFilname, 'w')

T=int(inpFile.readline())
for t in range(T):
    Line=inpFile.readline().strip()
    SList=list(Line.split(' ')[0])
    K=int(Line.split(' ')[1])
    
    #print K
    FlagFailed=True
    FlipperusedCounter=0
    for i in range(0,len(SList)-K+1):
        #print 'Slist= ',SList,' i =',i
        if SList[i]=='-':
            FlipperusedCounter+=1
            for j in range(K):
                if SList[i+j]=='-':
                    SList[i+j]='+'
                elif SList[i+j]=='+':
                    SList[i+j]='-'
        #print SList
        FlagFailed=False
        for  c in SList:
            if c=='-':
             FlagFailed=True
        if not FlagFailed:
            outFile.write("Case #%s: %s\n"%(t+1,FlipperusedCounter))
            break
            
    if FlagFailed:
        outFile.write("Case #%s: IMPOSSIBLE\n"%(t+1))
    
inpFile.close()
outFile.close()
    
