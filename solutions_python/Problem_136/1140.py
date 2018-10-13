#def getOptimumTime(C,F,X,PR):
inFile = open("B-large.in")
outFile = open("large.out","w")

T = inFile.readline()
T = int(T)

for num in range(0,T):
    line = inFile.readline()
    
    line = line.split(" ")
    
    C = float(line[0])
    F = float(line[1])
    X = float(line[2])
    
    PR = 2
    
    totalTime = 0
    
    while 1:
        timeToBuyFarm = C/PR
        
        
        timeToComp = X/PR
        
        
        nPR = PR + F
        
        if (timeToComp < timeToBuyFarm):
            totalTime += timeToComp;
            break
        
        timeToCompNext = X/nPR
        
        if ((timeToCompNext + timeToBuyFarm) > timeToComp):
            totalTime += timeToComp;
            break
        
        totalTime += timeToBuyFarm;
        PR += F
        
    outFile.write("Case #"+str(num+1)+": "+str(totalTime)+"\n")

inFile.close();
outFile.close();