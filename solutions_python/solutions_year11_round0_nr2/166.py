INPUT_FILE = r'C:\Downloads\FromFirefox\B-large.in'
OUTPUT_FILE = r'C:\Users\Assaf\Fun\codeJam\B-large.out'

inputFile = file(INPUT_FILE, 'rb')
numQuestions = int(inputFile.readline())
outputFile = file(OUTPUT_FILE, 'wb')

def solveQuestion(combain, disappear, elements):
    magicka = ['\x00']
    for element in elements:
        magicka.append(element)
        pair = magicka[-2] + magicka[-1]
        while pair in combain:
            magicka = magicka[:-2] + [combain[pair]]
            pair = magicka[-2] + magicka[-1]
        for d in disappear:
            if d[0] in magicka and d[1] in magicka:
                magicka = ['\x00']
    return `magicka[1:]`.replace("'", '').replace('"', '')   

for q in xrange(numQuestions):
    outputFile.write("Case #%d: " % (q+1))
    line = inputFile.readline().replace('\r', '').replace('\n', '').replace('\t', ' ').split(' ')
    C = int(line[0])
    line = line[1:]
    combain = {}
    for i in xrange(C):
        combain[line[0][:2]] = line[0][2]
        combain[line[0][:2][::-1]] = line[0][2]
        line = line[1:]
    D = int(line[0])
    line = line[1:]
    disappear = []
    for i in xrange(D):
        disappear.append((line[0][0], line[0][1]))
        line = line[1:]
    N = int(line[0])
    line = line[1:]
    if len(line[0]) != N:
        raise Exception("Input error at N")
    result = solveQuestion(combain, disappear, line[0])
    outputFile.write(result)
    outputFile.write("\n")

outputFile.close()
inputFile.close()
# print file(OUTPUT_FILE, 'rb').read()
