INPUT_FILE = r'C:\Downloads\FromFirefox\C-large.in'
OUTPUT_FILE = r'C:\Users\Assaf\Fun\codeJam\C-candy-large.out'

inputFile = file(INPUT_FILE, 'rb')
numQuestions = int(inputFile.readline())
outputFile = file(OUTPUT_FILE, 'wb')

def solveQuestion(vlaues):
    xorall = 0
    for x in values:
        xorall ^= x
    if 0 != xorall:
        return "NO"
    values.sort()
    return str(sum(values[1:]))

for q in xrange(numQuestions):
    outputFile.write("Case #%d: " % (q+1))
    N = int(inputFile.readline())
    values = map(int, inputFile.readline().split(' '))
    if len(values) != N:
        raise Exception("Input error at N")
    result = solveQuestion(values)
    outputFile.write(result)
    outputFile.write("\n")

outputFile.close()
inputFile.close()
# print file(OUTPUT_FILE, 'rb').read()
