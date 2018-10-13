import baker

def solveQuestion(smax, vals):
    total = 0
    needed = 0
    for i, x in enumerate(vals):
        if total < i and x > 0:
            toAdd = (i - total)
            needed += toAdd
            total += toAdd
        total += x
    return needed

def solveAll(inFile, outFile):
    numQuestions = int(inFile.readline())
    for q in xrange(numQuestions):
        outFile.write("Case #%d: " % (q+1))
        line = inFile.readline()
        smax, vals = line.split()
        smax = int(smax)
        vals = [int(x) for x in vals]
        result = solveQuestion(smax, vals)
        outFile.write(str(result))
        outFile.write("\n")

@baker.command
def run(inFile, outFile=None):
    if None == outFile:
        outFile = inFile + '.out'
    inFile = file(inFile, 'rb')
    outFile = file(outFile, 'wb')

    solveAll(inFile, outFile)

    outFile.close()
    inFile.close()

if __name__ == '__main__':
    baker.run()

