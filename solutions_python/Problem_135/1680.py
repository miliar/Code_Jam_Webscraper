
f = open ("input1.in","r")

def getAns(data1,data2,guess1,guess2,case):
    g1 = data1[guess1-1]
    g2 = data2[guess2-1]

    ans =0
    sameCnt =0
    for i in g1:
        if i in g2:
            ans =i
            sameCnt+=1
    

    if sameCnt >1:
        print "Case #" +str(case)+": Bad magician!"
    elif sameCnt ==0:
        print "Case #" +str(case)+": Volunteer cheated!"
    else:
        print "Case #" +str(case)+": "+str(ans)
    
    
case =1
tests = f.readline()
for i in range(int(tests)):
    data1 =[]
    guess1 = int(f.readline().strip())
    for x in range(4):
        data1.append(f.readline().strip().split())
    data2 =[]
    guess2 =int(f.readline().strip())
    for x in range(4):
        data2.append(f.readline().strip().split())
    
    getAns(data1,data2,guess1,guess2,case)
    case+=1