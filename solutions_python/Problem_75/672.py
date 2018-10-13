numTests = input()
for testCase in range(1, numTests+1):
    values = raw_input().split()
    merges = {}

    c = int(values.pop(0))
    for i in range(c):
        merge = values.pop(0)
        merges[merge[:2]] = merge[-1]

    b = int(values.pop(0))
    booms = {}
    for val in values[:b]:
        if booms.has_key(val[0]):
            booms[val[0]].append(val[1])
        else:
            booms[val[0]] = [val[1]]

        if booms.has_key(val[1]):
            booms[val[1]].append(val[0])
        else:
            booms[val[1]] = [val[0]]

    casts = values[-1]
    res = list(casts[:1])
    for cast in casts[1:]:
        res.append(cast)
        c = ''.join(res[-2:])
        if merges.has_key(c):
            res[-2:] = [merges[c]]
        elif merges.has_key(c[::-1]):
            res[-2:] = [merges[c[::-1]]]
        elif booms.has_key(cast):
            for l in res[:-1]:
                if l in booms[cast]:
                    res = []

    print "Case #%d: [%s]" % (testCase, ', '.join(res))
