import sys

T = int(sys.stdin.readline())

for _ in range(T):
    out = "Case #%d: " % (_ + 1)

    case = [ int (c) for c in sys.stdin.readline().split(' ')]
    numBoost = case[0]
    timeBoost = case[1]
    numStar = case[2]
    case = case[4:]
    path = []
    for __ in range(numStar):
        path.append(case[__ % len(case)])
    totalTime = 0
    if numBoost > 0:
        while len(path) >= 0:
            p = path.pop(0)
            if totalTime + p * 2 >= timeBoost:
                disLeft = (totalTime + p * 2 - timeBoost) / 2.0
                totalTime = timeBoost
                path.append(disLeft)
                break
            else:
                totalTime += p * 2
    for __ in range(numBoost):
        maxNum = max(path)
        totalTime += maxNum
        path.remove(maxNum)
    for p in path:
        totalTime += p * 2

    out += str (int(totalTime))
    print out

    
