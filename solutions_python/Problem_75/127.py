import sys
def input():
    sys.stdin.next()
    cases = []
    for line in sys.stdin:
        comb_map = {}
        oppose_map = {}
        input_str = ''
        line = line.strip()
        items = iter(line.split())
        c_num = int(items.next())
        for i in range(c_num):
            comb = items.next()
            comb_map[comb[:-1]] = comb[-1]
            comb_map[comb[:-1][::-1]] = comb[-1]
        o_num = int(items.next())
        for i in range(o_num):
            opp = items.next()
            oppose_map.setdefault(opp[0], set()).add(opp[1])
            oppose_map.setdefault(opp[1], set()).add(opp[0])
        items.next()
        input_str = items.next()
        cases.append((comb_map, oppose_map, input_str))
    return cases
            


def TryCombine(outputList, i, combineMap):
    result = combineMap.get(outputList[-1] + i)
    if result:
        outputList[-1] = result
        return True
    else:
        return False


def TryOppose(outputList, i, opposeMap):
    result = opposeMap.get(i)
    if result:
        if result.intersection(set(outputList)):
            outputList[:] = []
            return True

    return False


def GenerateOutputList(inputString, combineMap, opposeMap):
    outputList = []
    for i in inputString:
        if not outputList:
            outputList.append(i)
        else:
            res = TryCombine(outputList, i, combineMap) or TryOppose(outputList, i, opposeMap)
            if not res:
                outputList.append(i)

    return outputList


for index, case in enumerate(input()):
    combineMap, opposeMap, inputString = case
    l = GenerateOutputList(inputString, combineMap, opposeMap)
    l = ', '.join(l)
    l = '[%s]' % l
    print 'Case #%d: %s' % (index + 1, l)
