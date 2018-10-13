import sys
with open(sys.argv[1]) as f:
    cases = int(f.next())
    caseNum = 1
    for line in f:
        data = line.strip().split()
        combine = {}
        n = int(data[0])
        for x in range(1,n+1):
            a,b,c = list(data[x])
            if a not in combine:
                combine[a] = {b:c}
            else:
                combine[a][b] = c
            if b not in combine:
                combine[b] = {a:c}
            else:
                combine[b][a] = c
        oppose = {}
        m = int(data[n+1])
        for y in range(n+2,n+2+m):
            a,b = list(data[y])
            if a not in oppose:
                oppose[a] = [b]
            else:
                oppose[a].append(b)
            if b not in oppose:
                oppose[b] = [a]
            else:
                oppose[b].append(a)
        seq = list(data[-1])
        thelist = []
        lastChar = None
        while len(seq)>0:
            lastChar = seq[0]
            secondToLastChar = None
            thelist.append(lastChar)
            if len(thelist)>1:
                secondToLastChar = thelist[-2]
            del seq[0]
            while (lastChar in combine) and (secondToLastChar in combine[lastChar]):
                del thelist[-1]
                del thelist[-1]
                thelist.append(combine[lastChar][secondToLastChar])
                lastChar = thelist[-1]
                secondToLastChar = None
                if len(thelist)>1:
                    secondToLastChar = thelist[-2]
            if lastChar in oppose:
                for w in oppose[lastChar]:
                    if w in thelist[:-1]:
                        thelist = []
        print "Case #"+str(caseNum)+": ["+", ".join(thelist)+"]"
        caseNum += 1
