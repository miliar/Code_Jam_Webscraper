#inputFileName = "test.in"
inputFileName = "A-small-attempt0.in"
#inputFileName = "A-small-attempt1.in"
#inputFileName = "A-small-attempt2.in"
#inputFileName = "A-small-attempt3.in"
#inputFileName = "A-large.in"
outputFileName = inputFileName[:-3] + ".out"


def calDist(datas, x, N, avg):
    sum = 0
    for i in xrange(N):
        ch, cnt = datas[i][x]
        sum += abs(avg - cnt)
    return sum


def calcSingleTest(f):
    line = f.readline()
    N = int(line.split()[0])
    lines = []
    shrunks = []
    datas = []
    for i in xrange(N):
        line = f.readline()
        lines.append(line)
        l = len(line)
        ch = line[0]
        cnt = 0
        shrunk = ""
        data = []
        for p in xrange(l):
            if line[p] == ch:
                cnt += 1
            else:
                shrunk += ch
                data.append((ch, cnt))
                cnt = 0
                ch = line[p]
        shrunks.append(shrunk)
        datas.append(data)
        if shrunks[i] != shrunks[0]:
            return "Fegla Won"
    print shrunks
    print datas

    game_sum = 0
    for x in xrange(len(datas[0])):
        sum = 0.0
        for i in xrange(N):
            ch, cnt = datas[i][x]
            sum += cnt
        avg = sum / N
        avg0 = int(avg)
        avg1 = avg0 + 1
        sum0 = calDist(datas, x, N, avg0)
        sum1 = calDist(datas, x, N, avg1)
        game_sum += min(sum0, sum1)

    return game_sum


with open(inputFileName) as inpF:
    with open(outputFileName, 'w') as outF:
        line = inpF.readline()
        testsCount = int(line)
        for i in xrange(1, testsCount + 1):
            print '--------------------------------------------'
            res = calcSingleTest(inpF)
            outF.write('Case #{0}: {1}\n'.format(i, res))




