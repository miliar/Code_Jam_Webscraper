file = open("B-large.in")
n = int(file.readline())
import re
ans = open("1.out","wt")

for z in range(0,n):
    turnaround = int(file.readline())
    trainsa, trainsb, maxtrainsa, maxtrainsb = 0, 0, 0, 0
    print trainsa, trainsb, maxtrainsa, maxtrainsb
    numtrainsa, numtrainsb = [int(item) for item in file.readline().split(" ")]
    print numtrainsa, numtrainsb
    #Avoid list overflow
    aDepart = [10000]
    bDepart = [10000]
    aArrive = [10000]
    bArrive = [10000]
    for x in range(0,numtrainsa):
        train = re.sub("\n|\r","",file.readline()).split(" ")
        train[0] = train[0].split(":")
        train[0] = int(train[0][0])*60 + int(train[0][1])
        train[1] = train[1].split(":")
        train[1] = int(train[1][0])*60 + int(train[1][1]) + turnaround
        #print train
        aDepart.append(train[0])
        bArrive.append(train[1])
    for x in range(0,numtrainsb):
        train = re.sub("\n|\r","",file.readline()).split(" ")
        train[0] = train[0].split(":")
        train[0] = int(train[0][0])*60 + int(train[0][1])
        train[1] = train[1].split(":")
        train[1] = int(train[1][0])*60 + int(train[1][1]) + turnaround
        bDepart.append(train[0])
        aArrive.append(train[1])
        #print train
    aDepart.sort()
    aArrive.sort()    
    bDepart.sort()
    bArrive.sort()
    print aDepart
    print aArrive
    print bDepart
    print bArrive

    for x in range(0, 60*24):
        
        while aArrive[0] == x:
            aArrive.pop(0)
            trainsa -= 1
            maxtrainsa = max(trainsa, maxtrainsa)

        while bArrive[0] == x:
            bArrive.pop(0)
            trainsb -= 1
            maxtrainsb = max(trainsb, maxtrainsb)
        
        while aDepart[0] == x:
            aDepart.pop(0)
            trainsa += 1
            maxtrainsa = max(trainsa, maxtrainsa)

        while bDepart[0] == x:
            bDepart.pop(0)
            trainsb += 1
            maxtrainsb = max(trainsb, maxtrainsb)
    print "Case #%d: %d %d\n"%(z+1, maxtrainsa, maxtrainsb)
    ans.write("Case #%d: %d %d\n"%(z+1, maxtrainsa, maxtrainsb))
