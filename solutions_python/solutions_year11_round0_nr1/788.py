import sys

numTestCase = int( sys.stdin.readline() )

for _ in range(numTestCase) :
    out = "Case #%d: " % (_ + 1)
    inputList = sys.stdin.readline().strip().split(' ')
    orangeLoc = 1
    blueLoc = 1
    orangeTime = 0
    blueTime = 0
    pressButtonNotBefore = -1
    for __ in range(1, len(inputList), 2):
        color = inputList[__]
        loc = int(inputList[__ + 1])
        if color == 'O':
            timeUsed = abs (orangeLoc - loc) + 1
            orangeTime += timeUsed
            orangeLoc = loc
            orangeTime = max(orangeTime, pressButtonNotBefore + 1)
            pressButtonNotBefore  = orangeTime
        if color == 'B':
            timeUsed = abs (blueLoc - loc) + 1
            blueTime += timeUsed
            blueLoc = loc
            blueTime = max(blueTime, pressButtonNotBefore + 1)
            pressButtonNotBefore = blueTime
    out += str(max(blueTime, orangeTime))
    print out
