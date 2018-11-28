INPUT_FILE = r'D:\Downloads\FromChrome\B-large.in'
OUTPUT_FILE = r'D:\Assaf\Fun\GoogleCodeJam2012\B-large.out'

inputFile = file(INPUT_FILE, 'rb')
numQuestions = int(inputFile.readline())
outputFile = file(OUTPUT_FILE, 'wb')

def solveQuestion(x):
    x = map(int, filter(None, x.split(' ')))
    length = x[0]
    s = x[1]
    p = x[2]
    scores = x[3:]
    if len(scores) != length:
        raise Exception("Length doesn't much %d %d" % (length, len(scores)))
    result = 0
    for score in scores:
        if 0 == score:
            if p == 0:
                result += 1
            continue
        if 1 == score:
            if p == 1 or p == 0:
                result += 1
            continue
        scoreDiv = score // 3
        if 0 == (score % 3):
            if scoreDiv >= p:
                result += 1
            elif (0 < s) and scoreDiv + 1 >= p:
                result += 1
                s -= 1
        elif 1 == (score % 3):
            if scoreDiv + 1 >= p:
                result += 1
        elif 2 == (score % 3):
            if (scoreDiv + 1) >= p:
                result += 1
            elif (0 < s) and ((scoreDiv + 2) >= p):
                result += 1
                s -= 1

    return result

for q in xrange(numQuestions):
    outputFile.write("Case #%d: " % (q+1))
    x = inputFile.readline()
    result = solveQuestion(x)
    outputFile.write(str(result))
    outputFile.write("\n")

outputFile.close()
inputFile.close()
# print file(OUTPUT_FILE, 'rb').read()

