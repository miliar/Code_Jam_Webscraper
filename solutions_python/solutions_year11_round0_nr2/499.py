input1 = open(r"c:\googleCode\B-large.in")
output1 = open(r"c:\googleCode\magikaBig.txt", 'w')
lines = input1.readline()
T = int(lines.strip())

opp={}
def mOpp(aList):
    aopp = {}
    for key in aList:
        if key[0] not in aopp:
            aopp[key[0]]=[key[1]]
        else:
            tempL = aopp[key[0]]
            if key[1] not in tempL:
                aopp[key[0]].append(key[1])
        if key[1] not in aopp:
            aopp[key[1]]=[key[0]]
        else:
            tempL = aopp[key[1]]
            if key[0] not in tempL:
                aopp[key[1]].append(key[0])
    return aopp

com={}
def mCom(aList):
    acom ={}
    for key in aList:
        if key[0]>=key[1]:
            acom[key[:-1]]=key[-1]
        else:
            acom[key[1]+key[0]]=key[-1]
    return acom

caseN = 1
lines = input1.readline()
while lines !='':
    tempL = (lines.rstrip('\n')).split(' ')
    C = int(tempL[0])
    com = mCom(tempL[1:(C+1)])
    D = int(tempL[1+C])
    opp = mOpp(tempL[(2+C):(2+C+D)])       
    test = list(tempL[-1])
    R= []
    for key in test:
        if len(R)>0:
            if key >= R[-1]:
                tempk = key+R[-1]
            else:
                tempk = R[-1]+key

            if tempk in com:
                R.pop()
                R.append(com[tempk])
            else:
                R.append(key)
        else:
            R.append(key)       
    
        if len(R)>1 and R[-1] in opp:
            for key1 in R[:-1]:
                if key1 in opp[key]:
                    R=[]
                    break
    
    #print caseN, R
    print caseN, lines
    lines = input1.readline()
    
    result =''
    for key in R:
        result +=key+', '
    result=result.rstrip(', ')   

    #print result   
    output1.write("Case #"+str(caseN)+": ["+ result+"]\n")

    
    caseN +=1
output1.close()
input1.close()

