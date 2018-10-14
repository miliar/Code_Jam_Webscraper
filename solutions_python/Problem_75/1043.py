#fread=open('/home/think/Downloads/A-small-attempt0.in','r')
fread=open('B-small-attempt0.in','r')
fwrite=open('out.txt','w')

total_cases=fread.readline().strip()
for i in range(int(total_cases)):
    line1 = fread.readline().strip()
    l1= line1.split() 
    combineStringCount = int(l1[0])
    csc=0
    combineDic={}
    while(csc<combineStringCount):
        combineDic[ l1[csc+1][:-1]] = l1[csc+1][-1:]
        csc = csc+1
    
    opposedStringCount = int(l1[combineStringCount+1]) 
    osc=0
    opposed=[]
    while(osc<opposedStringCount):
        opposed.append(l1[osc+combineStringCount+2])
        osc = osc + 1
        
    inputStr= l1[-1:][0]
    #print inputStr
    #print opposed
    #print combineDic
    outStr=inputStr[0]
    j=1
    while(j<len(inputStr)):
        if(combineDic.has_key(outStr[-1]+inputStr[j])):
            outStr=outStr[:-1] + combineDic[ outStr[-1]+inputStr[j] ]
            
        elif( combineDic.has_key(inputStr[j] + outStr[-1] )):
            outStr=outStr[:-1] + combineDic[ inputStr[j] + outStr[-1] ]
        else:
            flag=0
            for elem in outStr:
                tempStr1 = elem+inputStr[j]
                tempStr2 = inputStr[j] + elem
                if tempStr1 in opposed or tempStr2 in opposed:
                    j=j+1
                    if(j<len(inputStr)):
                        outStr=inputStr[j]
                        flag=1
                    else:
                        outStr=""
                        flag=2
                        break
            if (flag== 0):    
                outStr=outStr+inputStr[j]
            elif (flag==2):
                break
        j= j+1
    finalStr="["
    for o in outStr: 
        finalStr=finalStr + o +", "
    finalStr=finalStr.rstrip(", ") + "]"
    o_string="Case #"+str(i+1)+": "+finalStr+"\n"
    #print o_string
    fwrite.write(o_string)
       

    
fread.close()
fwrite.close()
