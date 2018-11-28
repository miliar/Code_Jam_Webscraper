import sys

def game(length, Naomi, Ken):
    global nTime
    nTime += 1
    Naomi.sort()
    Ken.sort()
    scoreWarKen = 0
    indexNaomi = 0
    for i in xrange(length):
        if Ken[i] > Naomi[indexNaomi]:
            scoreWarKen += 1
            indexNaomi += 1
    scoreWarNaomi = length - scoreWarKen

    scoreDeceitfulWarKen = 0
    indexNaomi = length - 1
    for i in xrange(length):
        indexKen = length - 1 - i
        if (Ken[indexKen] > Naomi[indexNaomi]):
            scoreDeceitfulWarKen += 1
        else:
            indexNaomi -= 1
    scoreDeceitfulWarNaomi = length - scoreDeceitfulWarKen
    sys.stdout.write('Case #' + str(nTime) + ': ' + str(scoreDeceitfulWarNaomi) + ' ' + str(scoreWarNaomi) + '\n')

            


def readLine(inputFile):
    for line in inputFile:
        yield line.strip()

def main():
    global nTime
    nTime = 0
    data = readLine(sys.stdin)

    ifFirstLine = True
    line = 0
    for dataLine in data:
        if ifFirstLine:
            ifFirstLine = False
        else:
            if line == 0:
                length = int(dataLine)
            if line == 1:
                Naomi = [float(item) for item in dataLine.split(' ')]
            if line == 2:
                Ken = [float(item) for item in dataLine.split(' ')]
            line += 1
            if line == 3:
                game(length, Naomi, Ken)
                line = 0






if __name__ == '__main__':
    main()