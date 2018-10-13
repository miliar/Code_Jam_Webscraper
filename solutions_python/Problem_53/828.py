def checkNumber(k, n):
    if ((k % 2**n) == (2**n -1)):
        return True
    else:
        return False

def printResult(result, index):
    txtResult = "OFF"
    if (result):
        txtResult = "ON"

#    print "Case #" + str(index) + ": " + txtResult
    outFile.write("Case #" + str(index) + ": " + txtResult + "\n")

inFile = file("input.txt")
outFile = file("output.txt", "w")

numTest = inFile.readline()

for i in xrange(1, int(numTest) + 1):
    currLine = inFile.readline()
    n,null ,k = currLine.partition(' ')
    n = int(n)
    k = int(k)
    printResult(checkNumber(k,n), i)

outFile.close()
inFile.close()
