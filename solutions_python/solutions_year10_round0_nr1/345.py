import string

def solve (inputs):
    (n, k) = (int (i) for i in inputs)
    isOn = (k + 1) % 2**n == 0
    if (isOn):
        return ("ON")
    else:
        return ("OFF")

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

