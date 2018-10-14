def fun(distance, horseList):
    maxTime = 0
    for start, speed in horseList:
        time = (distance - start) * 1.0 / speed
        if time > maxTime:
            maxTime = time
    return distance / maxTime

n = int(raw_input())
for i in range(n):
    distance, horseCount = map(int, raw_input().strip().split(' '))
    horseList = []
    for j in range(horseCount):
        horseList.append(map(int, raw_input().strip().split(' ')))
    print "Case #{0}: {1:.7f}".format(i+1, fun(distance, horseList))
