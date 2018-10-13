def draw(simpleColorList, superColorList):
    extra = - max(simpleColorList) * 2 + sum(simpleColorList)
    simpleColorList = [simpleColorList[0] - extra, simpleColorList[1] - extra, simpleColorList[2] - extra]
    if simpleColorList[0] >= simpleColorList[1] and simpleColorList[0] >= simpleColorList[2]:
        tempList = ['R', 'Y', 'B'] * extra
        tempList.extend(['R', 'Y'] * simpleColorList[1])
        tempList.extend(['R', 'B'] * simpleColorList[2])
    elif simpleColorList[1] >= simpleColorList[2]:
        tempList = ['Y', 'R', 'B'] * extra
        tempList.extend(['Y', 'R'] * simpleColorList[0])
        tempList.extend(['Y', 'B'] * simpleColorList[2])
    else:
        tempList = ['B', 'R', 'Y'] * extra
        tempList.extend(['B', 'R'] * simpleColorList[0])
        tempList.extend(['B', 'Y'] * simpleColorList[1])
    if superColorList[0] > 0:
        for i in range(len(tempList)):
            if tempList[i] == 'R':
                tempList[i] = 'RG' * superColorList[0] + 'R'
                break
    if superColorList[1] > 0:
        for i in range(len(tempList)):
            if tempList[i] == 'Y':
                tempList[i] = 'YV' * superColorList[1] + 'Y'
                break
    if superColorList[2] > 0:
        for i in range(len(tempList)):
            if tempList[i] == 'B':
                tempList[i] = 'BO' * superColorList[2] + 'B'
                break
    return ''.join(tempList)

def fun(countList):
    #countList: [0:count 1:R 2:O 3:Y 4:G 5:B 6:V]
    #superColorList: [0:R, 1:Y, 2:B]
    countList[0] = 0
    superColorList = [0, 0, 0]
    if countList[4] > 0 and countList[1] < countList[4] + 1:
        if countList[1] == countList[4] and sum(countList) == 2 * countList[1]:
            return "RG" * countList[1]
        else:
            return "IMPOSSIBLE"
    else:
        superColorList[0] = countList[4]
        countList[1] -= countList[4]
        countList[4] = 0
    if countList[6] > 0 and countList[3] < countList[6] + 1:
        if countList[3] == countList[6] and sum(countList) == 2 * countList[3]:
            return "YV" * countList[3]
        else:
            return "IMPOSSIBLE"
    else:
        superColorList[1] = countList[6]
        countList[3] -= countList[6]
        countList[6] = 0
    if countList[2] > 0 and countList[5] < countList[2] + 1:
        if countList[5] == countList[2] and sum(countList) == 2 * countList[5]:
            return "BO" * countList[5]
        else:
            return "IMPOSSIBLE"
        countList[5] -= countList[2]
        countList[2] = 0
    simpleColorList = [countList[1], countList[3], countList[5]]
    if max(simpleColorList) * 2 > sum(simpleColorList):
        return "IMPOSSIBLE"
    else:
        return draw(simpleColorList, superColorList)

n = int(raw_input())
for i in range(n):
    colorList = map(int, raw_input().strip().split(' '))
    print "Case #{0}: {1}".format(i+1, fun(colorList))
