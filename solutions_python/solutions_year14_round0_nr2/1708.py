import time,sys

lines = [line.strip() for line in open('input2.txt')]

testCase = lines[0]
testCase = int(testCase)

output = ""

if testCase < 1 or testCase > 100:
    print("Test case not in range")
    sys.exit()

for x in range(0, int(testCase)):
    curLine = lines[x + 1].split()

    farmCost = float(curLine[0])
    farmAdd = float(curLine[1])
    until = float(curLine[2])
    
    myCook = 0.0
    curRate = 2.0

    output = until / curRate
    #print("no Bought: " + str(output))

    for y in range(0, 50000):
        #print("Will Buy: " + str(y))
        curRate = 2.0
        totalTime = 0.0
        for z in range(0, y):
            totalTime = totalTime + (farmCost/curRate)
            curRate = curRate + farmAdd
            #print("cR: " + str(curRate) + " tT: " +str(totalTime) + " fC: " + str(farmCost))

        totalTime = (until / curRate) + totalTime
        #print("#Total: " + str(totalTime))

        if totalTime < output:
            output = totalTime

        if totalTime > output:
            break

    print("Case #" + str(x + 1) + ": %0.7f" % output)

    

