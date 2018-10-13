#!/usr/bin/python
with open("B-small-attempt2.in") as f:
    testCases = []
    lines = f.read().split("\n")[1:-1]
    i = 0
    for case in lines:
        i += 1
        N, R, O, Y, G, B, V = [int(x) for x in case.split(" ")]
        # pure: R, Y, B
        # O: RY
        # G: YB
        # V: RB
        allR = R + O + V
        allY = Y + O + G
        allB = B + G + V
        data = {"R": R, "O": O, "Y": Y, "G": G, "B": B, "V": V}
        nexts = {"O": "B", "G": "R", "V": "Y"}
        maxColor = max([allR, allY, allB])
        if maxColor > N / 2 or O + G + V > N / 2:
            print("Case #%d: IMPOSSIBLE" % i)
            continue
        outStr = ""
        imp = 0
        maxT = max([data['O'], data['G'], data['V']])
        if maxT == 0:
            nextS = data.keys()[data.values().index(max(data.values()))]
            outStr += nextS
            data[nextS] -= 1
        while maxT > 0:
            maxN = data.keys()[data.values().index(maxT)]
            outStr += maxN
            data[maxN] -= 1
            nextU = nexts[maxN]
            if data[nextU] < 1:
                print("Case #%d: IMPOSSIBLE" % i)
                imp = 1
                break
            outStr += nextU
            data[nextU] -= 1
            maxT = max([data['O'], data['G'], data['V']])
            if maxT == 0:
                nextS = nextU
                break
            prevMaxN = maxN
            maxN = data.keys()[data.values().index(maxT)]
            if prevMaxN is maxN:
                continue
            if data[nexts[maxN]] < 2 and sum(data.values()) > 2 or data[nexts[maxN]] < 1:
                print("Case #%d: IMPOSSIBLE" % i)
                imp = 1
                break
            outStr += nexts[maxN] + maxN
            data[nexts[maxN]] -= 1
            data[maxN] -= 1
            maxT = max([data['O'], data['G'], data['V']])
            if maxT < 1:
                nextS = nexts[maxN]
                outStr += nextS
                data[nextS] -= 1
        if imp:
            continue

        mustLeave = nexts[outStr[0]] if outStr[0] in nexts else max([x for x in data.iteritems() if x[0] in list(set("RYB") - set(outStr[0]))], key=lambda x: x[1])[0]
        if data[mustLeave] == 0:
            print("Case #%d: IMPOSSIBLE" % i)
            continue
        data[mustLeave] -= 1
        while sum(data.values()) > 0:
            nextI = max([x for x in list(data.iteritems()) if x[0] is not outStr[-1]], key=lambda x: x[1])
            if sum(data.values()) == 1 and nextI[0] is mustLeave:
                if "".join([x for x in list("RYB") if x is not nextI[0]]) in outStr:
                    ind = outStr.index("".join([x for x in list("RYB") if x is not nextI[0]])) + 1
                    outStr = outStr[0:ind] + nextI[0] + outStr[ind:len(outStr)]
                elif "".join(reversed([x for x in list("RYB") if x is not nextI[0]])) in outStr:
                    ind = outStr.index("".join(reversed([x for x in list("RYB") if x is not nextI[0]]))) + 1
                    outStr = outStr[0:ind] + nextI[0] + outStr[ind:len(outStr)]
                else:
                    print("Case #%d: IMPOSSIBLE" % i)
                    imp = 1
                break
            outStr += nextI[0]
            data[nextI[0]] -= 1
        if imp:
            continue
        outStr += mustLeave

        print("Case #%d: %s" % (i, outStr))
