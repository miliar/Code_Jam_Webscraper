T = input()
testNum = 1
totalTestNum = int(T)
while (testNum <= totalTestNum):
    line = input()
    part = line.split(' ');
    maxS = int(part[0])
    shyLevels = part[1]
    audNum = 0

    if maxS == 0:
        print("Case #%d: 0" %testNum)
        testNum = testNum + 1
        continue
    
    tempSum = 0
    for shyLevel in range(0, len(shyLevels)):
        delta = 0
        shyLevelNum = int(shyLevels[shyLevel])
        if shyLevelNum > 0 and tempSum < shyLevel:
            delta = (shyLevel - tempSum)
            audNum = audNum + delta
        tempSum = tempSum + shyLevelNum + delta

    print("Case #%d: %d" %(testNum, audNum))
    testNum = testNum + 1
