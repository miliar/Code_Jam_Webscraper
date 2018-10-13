

def main():
    testFile = open("test.txt")
    numCases = int(testFile.readline())
    for i in range(numCases):
        testFile.readline()
        arr = map(int, testFile.readline().split(' '))
        outOfOrder = 0
        for (j, x) in enumerate(arr):
            if j + 1 != x:
                outOfOrder += 1
        print("Case #%d: %d" % (i + 1, outOfOrder))

main()
