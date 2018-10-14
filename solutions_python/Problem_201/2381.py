def getLs(stalls, index):
    count = 0
    for i in range(index-1, 0, -1):
        if stalls[i] == '':
            count += 1
        else:
            return count
    return count

def getRs(stalls, index):
    count = 0
    for i in range(index+1, len(stalls)):
        if stalls[i] == '':
            count += 1
        else:
            return count
    return count

def calculateRsLs(stalls):
    d = {}
    for i in range(len(stalls)):
        if stalls[i] == '':
            d[i] = [getLs(stalls, i), getRs(stalls, i)]
    return d


def chooseStall(d):
    mins = []
    for key, values in d.iteritems():
        mins.append(min(values[0], values[1]))
    maximum = max(mins)
    options = {}
    for key, values in d.iteritems():
        if min(values[0], values[1]) == maximum:
            options[key] = values

    if len(options) > 1:
        maxs = []
        for key, values in options.items():
            maxs.append(max(values))
        maximum = max(maxs)
        options2 = {}
        for key, values in options.items():
            if max(values) == maximum:
                options2[key] = values
                return min(options2)
    else:
        return min(options)

t = int(raw_input())  # read a line with a single integer

for i in xrange(1, t + 1):
    n, k = [int(s) for s in raw_input().split(" ")]

    stalls = ['.']
    for j in range(n):
        stalls.append('')
    stalls.append('.')

    maxLsRs = -1
    minLsRs = -1
    for p in range(k):
        LsRsDict = calculateRsLs(stalls)
        indexOfChosen = chooseStall(LsRsDict)
        maxLsRs = max(getLs(stalls, indexOfChosen), getRs(stalls, indexOfChosen))
        minLsRs = min(getLs(stalls, indexOfChosen), getRs(stalls, indexOfChosen))
        stalls[indexOfChosen] = '.'

    print "Case #{}: {} {}".format(i, maxLsRs, minLsRs)
