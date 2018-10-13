
f = open("pass.txt")

fw = open("pass_output.txt","w")


n = int(f.readline())

caseNum = 0
for i in range(1,n+1):
    caseNum +=1
    info1 = f.readline().replace("\n","").split(" ")
    
    already = int(info1[0])
    total = int(info1[1])
    
    info2 = f.readline().replace("\n","").split(" ")
    
    
    
     
    
    #print already
    #print total
   
    
    rekey = float( total + 1.000000)
    expBack = []
    
    for j in range(0,int(already * 0.5 + 1)):
        expBack.append(float(j * 2 + (total - already) + 1))
    #print expBack
    
    
    
    failChance = float(1.000000)
    
    for j in range(0,already):
        chance = float(info2[j])
        failChane = failChance * (1 - chance) 
        plusExp = failChane * rekey
        for k in range(0,min(len(expBack),already - j)):
            expBack[k] += plusExp
            
    rekey += 1    
    
    minExp = rekey
    for j in expBack:
        if j < minExp:
            minExp = j
    #print expBack
    #print rekey
    #print minExp
    fw.write("Case #" + str(caseNum) + ": "+ str(minExp) +"\n")    
        