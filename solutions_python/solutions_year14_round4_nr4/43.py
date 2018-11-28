__author__ = 'dan'

def possibilities(strings, servers):
    if strings == 0:
        return []
    if strings == 1:
        return [[x] for x in range(servers)]

    minusone = possibilities(strings-1, servers)
    toReturn = []
    for x in minusone:
        for i in range(servers):
            toReturn.append(x + [i])
    return toReturn

def prefixes(str):
    toReturn = set([])
    for i in range(len(str)+1):
        toReturn.add(str[:i])
    return toReturn

def evaluate(singleset):
    allprefixes = set([])
    for x in singleset:
        allprefixes |= prefixes(x)
    return len(allprefixes)

T = int(raw_input())
for case in range(1, T+1):
    M, N = map(int, raw_input().split())
    strings = []
    for _ in range(M):
        strings.append(raw_input())

    worst = 0
    worstCount = 0

    for poss in possibilities(M, N):
        sets = []
        for i in range(N):
            sets.append([])

        for i, str in enumerate(strings):
            sets[poss[i]].append(str)

        total = sum(map(evaluate, sets))

        if total == worst:
            worstCount += 1
        elif total > worst:
            worst = total
            worstCount = 1
    print "Case #%d: %d %d" % (case, worst, worstCount)












