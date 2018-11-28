def getToken(filename):
    inputFile = open(filename, 'r')
    for line in inputFile:
        tokens = line.split()
        for token in tokens:
            if token != '':
                yield token
    inputFile.close()

inputFilename = 'C-small-attempt0.in'
outputFilename = 'C-small-attempt0.txt'

tokenIterator = getToken(inputFilename)
def get():return tokenIterator.next()
def getint(): return int(get())
outputFile = open(outputFilename, 'w')

# END PRE-PROCESSING

caseNum = getint()
for case in range(caseNum):

    items = []
    x = 0

    itemNum = getint()
    for tt in range(itemNum):
        s = getint()
        items.append(s)
        x ^= s
    if x == 0:
        items.sort()
        answer = sum(items)-items[0]
        output = "Case #"+str(case+1)+": "+str(answer)
    else:
        output = "Case #"+str(case+1)+": NO"

    outputFile.write(output+"\n")

# BEGIN POST-PROCESSING
outputFile.close()

