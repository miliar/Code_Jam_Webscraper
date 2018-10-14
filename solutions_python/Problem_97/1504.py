def isRecycled(n, m):
    ns = str(n)
    ms = str(m)
    for shift in range(1, len(str(n)) + 2):
        newN = ns[shift:] + ns[:shift]
        if newN == ms:
            return True
    return False



inputFilename = "C-small-attempt1.in"
f = open(inputFilename, "r+")
output = ""

numCases = int(f.readline())

for lineNum, line in enumerate(f):
    print(lineNum)
    numbers = line.split(" ")
    A = int(numbers[0])
    B = int(numbers[1])

    count = 0
    for n in range(A, B):
        for m in range(n + 1, B + 1):
            if isRecycled(n, m):
                count += 1

    output += "Case #" + str(lineNum + 1) + ": " + str(count) + "\n"



outputFilename = "output.txt"
outputFile = open(outputFilename, "w")
outputFile.write(output)
outputFile.close()
f.close()

