import re, string, sys, os

output = ''
outFile = "large_result.out"
strIn = []

lineNum = 0
T = 0
strNum = 0
caseNum = 0
emptyFlag = 0

os.chdir(os.path.dirname(__file__))

def rowOper(strNum):
    xCnt = strIn[strNum].count('X')
    oCnt = strIn[strNum].count('O')
    tCnt = strIn[strNum].count('T')

    if xCnt + tCnt == 4:
        return 1
    elif oCnt + tCnt == 4:
        return 2

    return 0

def slashOper():
    rxCnt = 0
    roCnt = 0
    rtCnt = 0

    lxCnt = 0
    loCnt = 0
    ltCnt = 0

    for i in xrange(4):
        j = i + 1
        rStr = strIn[i][i]

        k = 3 - i
        lStr = strIn[i][k]

        if rStr == 'X':
            rxCnt += 1
        elif rStr == 'O':
            roCnt += 1
        elif rStr == 'T':
            rtCnt += 1

        if lStr == 'X':
            lxCnt += 1
        elif lStr == 'O':
            loCnt += 1
        elif lStr == 'T':
            ltCnt += 1

    if rxCnt + rtCnt == 4:
        return 1
    elif roCnt + rtCnt == 4:
        return 2
    elif lxCnt + ltCnt == 4:
        return 1
    elif loCnt + ltCnt == 4:
        return 2
    return 0

def colOper():
    for i in xrange(4):
        xCnt = 0
        oCnt = 0
        tCnt = 0

        for j in xrange(4):
            if strIn[j][i] == 'X':
                xCnt += 1
            elif strIn[j][i] == 'O':
                oCnt += 1
            elif strIn[j][i] == 'T':
                tCnt += 1

        if xCnt + tCnt == 4:
            return 1
        elif oCnt + tCnt == 4:
            return 2

    return slashOper()

def result_output(num, result):
    global output

    output += 'Case #%d: ' % (num + 1)

    if result == 1:
        output += 'X won\n'
    elif result == 2:
        output += 'O won\n'
    elif result == 0:
        if emptyFlag == 1:
            output += 'Game has not completed\n'
        else:
            output += 'Draw\n'
    return

def result_fout():
    global output

    try:
        fd = open(outFile, 'w+')
    except:
        print 'Fail to open %s.' % outFile
        sys.exit(-1)

    fd.write(output)
    fd.close()
    return


base_file = sys.argv[1]
try:
    base_fd = open(base_file, 'r')
except:
    print 'Fail to open %s.' % base_file
    sys.exit(-1)

for line in base_fd:
    if T == 0:
        T = int(line)
    else:
        if result == 0:
            line = re.sub(r'\r|\n|\)', '', line)
            if len(line) == 0:
                continue

            strIn.append(line)

            if '.' in line:
                emptyFlag = 1

            result = rowOper(strNum)
            if result != 0:
                result_output(caseNum, result)

        strNum += 1

    if strNum == 4:
        if result == 0:
            result = colOper()
            result_output(caseNum, result)

        strNum = 0
        strIn = []
        result = 0
        emptyFlag = 0
        caseNum += 1

result_fout()
