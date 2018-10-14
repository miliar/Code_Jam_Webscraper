inputstr="""3 5 4
abc
bca
dac
dbc
cba
(ab)(bc)(ca)
abc
(abc)(abc)(abc)
(zyx)bc"""


FileIn=open("A-large.in","r")

content=FileIn.read()
content=content.split('\n')


print content[0]
line=content[0].split(' ')

wordLen=int(line[0])
caseCounter=int(line[1])
patternCounter=int(line[2])

index=1

caseList=[]
for i in range(caseCounter):
    caseList.append(content[index])
    index=index+1

patternList=[]
for j in range(patternCounter):

    pattern=[]
    line=content[index]
    k=0
    while(k<len(line)):
        tmpPattern=[]
        if(line[k]=='('):
            while(line[k]!=')'):
                tmpPattern.append(line[k])
                k=k+1
            k=k+1
        else:
            tmpPattern.append(line[k])
            k=k+1
        pattern.append(tmpPattern)
    

    

    """
    line=content[index]
    line=line.split('(')
    pattern=[]
    for k in range(len(line)):
        if(line[k]==''):
            pass
        else:
            if(line[k].endswith(')')):
                tmpPattern=[]
                for v in range(len(line[k])):
                    if(line[k][v]==')'):
                        continue
                    else:
                        tmpPattern.append(line[k][v])
                pattern.append(tmpPattern)
                
                
            else:
                
                for v in range(len(line[k])):
                    tmpPattern=[]
                    tmpPattern.append(line[k][v])
                    pattern.append(tmpPattern)

    
    """                
    if(len(pattern)>wordLen):
        print "ERROR detected!"
        print pattern
        print len(pattern)
        print line
    patternList.append(pattern)
    index=index+1
   

#print patternList


FileOut=open("result.out",'w')

    
for j in range(len(patternList)):
    matchCounter=0
    for i in range(len(caseList)):
        
        matchFlag=True
        #print "~~~~~"
        #print patternList[j]
        #print "xxxxx"
        #print caseList[i]
        for k in range(len(caseList[i])):
            if(patternList[j][k].count(caseList[i][k])==0):
                #print patternList[j][k]
                #print caseList[i][k]
                matchFlag=False    
                break
            
        if matchFlag==True:
            matchCounter=matchCounter+1
    FileOut.write("Case #"+str(j+1)+": "+str(matchCounter)+"\n")


FileOut.close()

#print "~~~~~~~~~~~~~~`"
#print len(caseList)
        
    

    
