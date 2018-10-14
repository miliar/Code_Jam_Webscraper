inputs = open("inputs.txt", 'r')
outputs = open("outputs.txt", 'w')
nCases = int(inputs.readline())

for case in range(1, nCases+1):
    clues = inputs.readline()
    clues = clues.split()
    farmCost = float(clues[0])
    farmYield = float(clues[1])
    endGame = float(clues[2])
    
    reqFarms = 0
    bestTime = endGame/2

    while True:
        reqFarms += 1
        curTime = 0
        countRate = 2

        for j in range(reqFarms):
            curTime += farmCost/countRate
            countRate += farmYield

        curTime += endGame/countRate

        if curTime >= bestTime:
            break
        elif curTime < bestTime:
            bestTime = curTime

    outputs.write("Case #" + str(case) + ": " + str(bestTime) + "\n")
    
inputs.close()
outputs.close()
