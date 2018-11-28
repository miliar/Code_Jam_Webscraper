import string
import fractions

def solve (inputs):
    inputs = [int (i) for i in inputs]
    n = inputs.pop(0)
    first = inputs.pop(0)
    inputs = [i - first for i in inputs]
    gcd = inputs.pop(0)
    for i in inputs:
        gcd = fractions.gcd(gcd, i)
    ans = -abs(first) % abs(gcd)
    return (str(ans))

def go ():
    inFileName = raw_input("in: ")
    outFileName = raw_input("out: ")

    inFile = open(inFileName, 'r')
    outFile = open(outFileName, 'w')

    testCases = int(string.strip(inFile.readline()))

    for t in range(1, testCases + 1):
        line = inFile.readline()
        inputs = string.split(line)
        solution = solve (inputs)
        outFile.write("Case #%d: %s\n" % (t, solution))

    outFile.close()
    inFile.close()
