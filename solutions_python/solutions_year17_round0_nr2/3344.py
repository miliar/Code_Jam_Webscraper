InputFilename='B-large.in'
OutputFilname=InputFilename.replace("in","out")
#print OutputFilname
inpFile = open(InputFilename, 'r')
outFile = open(OutputFilname, 'w')

T=int(inpFile.readline())
for t in range(T):
    N=inpFile.readline().strip()
    NList=list(N)
    #print N
    for cc in NList:
        flagNines=False
        oldChar='0'
        for idx, c in enumerate(NList):
            #print ('oldchar = %s C= %s idx= %s'%(oldChar,c,idx))
            if (ord(c)<ord(oldChar))and (not flagNines):
                NList[idx-1]=str(ord(NList[idx-1])-ord('1'))
                flagNines=True
                #print('Flag is True')
            if flagNines==True:
                NList[idx]='9'           
            oldChar=c
        if flagNines==False:
            break
    outFile.write("Case #%s: %s\n"%(t+1,int(''.join(NList))))
    
inpFile.close()
outFile.close()
    
