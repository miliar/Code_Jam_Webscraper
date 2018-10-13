import sys

def readLine(inputFile):
    for line in inputFile:
        yield line.strip()

def calTime2(num, C, F, X):
    result = 0
    i = -1
    for i in xrange(num):
        result += C / (2.0 + i * F)
    i += 1
    result1 = result +  X / (2.0 + i * F)
    result2 = result + C / (2.0 + i * F) + X / (2.0 + (i + 1) * F)
    if result1 < result2:
        return result1
    return result2


def main():
    nTime = 0
    data = readLine(sys.stdin)

    ifFirstLine = True
    for dataLine in data:
        if ifFirstLine:
            ifFirstLine = False
        else:
            nTime += 1
            dataLine = dataLine.split(' ')
            C = float(dataLine[0])
            F = float(dataLine[1])
            X = float(dataLine[2])
            # print dataLine
            Ncal = int(X/C - 2/F)
            N = max(1, Ncal)
            a = calTime2(N - 1, C, F, X)
            sys.stdout.write('Case #' + str(nTime) + ': ' + str(a) + '\n')






if __name__ == '__main__':
    main()