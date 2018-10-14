from collections import defaultdict
T = int(raw_input())

for case in xrange(1, T+1):
    items = raw_input().split()
    C = int(items[0])
    D = int(items[C+1])

    combinations = defaultdict(lambda: defaultdict(lambda: None))
    competative = defaultdict(lambda: defaultdict(lambda: False))

    for comb in items[1:C+1]:
        combinations[comb[0]][comb[1]] = comb[2]
        combinations[comb[1]][comb[0]] = comb[2]

    for pair in items[C+2:C+D+2]:
        competative[pair[0]][pair[1]] = True
        competative[pair[1]][pair[0]] = True

    result = []
    for elem in items[-1]:
        result.append(elem)
        if len(result) >= 2:
            if combinations[result[-1]][result[-2]]:
                t = combinations[result[-1]][result[-2]]
                result.pop()
                result.pop()
                result.append(t)
        for i in xrange(len(result)-1):
            if competative[result[-1]][result[i]]:
                result = []
                break

    print "Case #%d:"%case, "[" + ", ".join(result) + "]"


