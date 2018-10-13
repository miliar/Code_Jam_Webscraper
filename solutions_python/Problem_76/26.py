

def getResult(values):
    xord = 0
    for v in values:
        xord = xord ^ v
    if xord != 0:
        return None
    return sum(values) - min(values)

def main():
    testFile = open("test.txt")
    numCases = int(testFile.readline())
    for i in range(numCases):
        testFile.readline()
        values = map(int, testFile.readline().split(' '))
        result = getResult(values)
        output = "NO"
        if result != None:
            output = str(result)
        print("Case #%d: %s" % (i + 1, output))

main()
