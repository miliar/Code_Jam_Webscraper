import math

INPUT_FILE = r'D:\Downloads\FromChrome\C-small-attempt0.in'
OUTPUT_FILE = r'D:\Assaf\Fun\GoogleCodeJam2012\C-small-attempt0.out'

inputFile = file(INPUT_FILE, 'rb')
numQuestions = int(inputFile.readline())
outputFile = file(OUTPUT_FILE, 'wb')

def solveQuestion(bottom, top):
    result = 0
    numDigits = int(math.log(bottom, 10)) + 1
    for x in range(bottom, top):
        founds = []
        for d in range(1, numDigits):
            p = (10 ** d)
            q = (10 ** (numDigits - d))
            t = x // p
            t += (x - (t * p)) * q
            if x < t and t <= top and (t not in founds):
                result += 1
                founds.append(t)
    return result

for q in xrange(numQuestions):
    outputFile.write("Case #%d: " % (q+1))
    x, y = map(int, filter(None, inputFile.readline().split(' ')))
    result = solveQuestion(x, y)
    outputFile.write(str(result))
    outputFile.write("\n")

outputFile.close()
inputFile.close()
# print file(OUTPUT_FILE, 'rb').read()

