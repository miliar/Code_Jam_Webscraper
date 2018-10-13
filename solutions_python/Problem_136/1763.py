#Reading and opening file in data
with open ("B-small-attempt0.in", "r") as myfile:
    data=myfile.readlines()
myfile.close()

counter = 0
for d in data:
    if str(d[len(d)-1:len(d)+1]) == "\n":
        data[counter] = d[:len(d)-1]
    counter +=1


numData = int(data[0])
del data[0]
for i in range(0, numData):
    usingData = data[0]
    usingData = usingData.split()
    farmCost = float(usingData[0])
    extraCookie = float(usingData[1])
    endCookie = float(usingData[2])
    prevanswer = 0
    newanswer = endCookie/2
    numFarm = 0
    flag = 1
    while flag == 1:
        prevanswer = newanswer
    
        numFarm+=1
        newanswer = 0
        for j in range(0,numFarm):
            newanswer+=farmCost/(2+extraCookie*j)
        newanswer+=endCookie/(2+extraCookie*numFarm)
        if newanswer>prevanswer:
            flag = 0
    print "Case #"+str(i+1)+": "+str(prevanswer)
    del data[0]
