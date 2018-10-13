'''
Created on 08.05.2010
'''
import fractions

def getResult(inputsList):
    print inputsList
    diffs=[]
    for i in range(len(inputsList)):
        diff=abs(inputsList[i]-inputsList[i-1])
        if diff==1:
            return 0
        if diff>1:
            diffs.append(diff)
    m=diffs[0]
    for j in range(1,len(diffs)):
        m=fractions.gcd(m,diffs[j])
        if m==1:
            return 0
    #print diffs
    #print m
    return (m-inputsList[0]%m)%m

inputFile="B-large.in"
outputFile=open(inputFile.split(".")[0]+".out",'w')
input=open(inputFile)
caseNum=0
lineCount=0
for line in input:
    inputs=[]
    if lineCount==0:
        caseNum=int(line)
        lineCount+=1
    else:
        str_inputs=line.split()
        for str_input in str_inputs[1:]:
            inputs.append(int(str_input))
        result="Case #"+str(lineCount)+": "+str(getResult(inputs))
        print result
        lineCount+=1
        outputFile.write(result+"\n")

input.close()
outputFile.close()



