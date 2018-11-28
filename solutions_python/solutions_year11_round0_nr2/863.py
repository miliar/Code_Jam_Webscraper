T = int(raw_input())

for t in xrange(T):
    line = raw_input().split()
    C = int(line[0])
    D = int(line[C + 1])
    combine = {}
    for i in xrange(1, C + 1):
        b1, b2, nb = list(line[i])
        combine[b1 + b2] = nb
        combine[b2 + b1] = nb
    oppose = line[C+2:C+D+2]
    N = int(line[-2])
    invoke = list(line[-1])
    result = []
    for element in invoke:
        result.append(element)
        if len(result) < 2:
            continue
        if combine.has_key(result[-1] + result[-2]):
            combination = combine[result[-1] + result[-2]]
            del result[-2:]
            result.append(combination)
        for a, b in oppose:
            if a in result and b in result:
                result = []
    
    print "Case #%i: %s" % (t + 1, repr(result).replace("'", ""))