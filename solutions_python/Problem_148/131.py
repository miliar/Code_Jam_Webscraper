inputFile = open('A-large.in', 'r')
outputFile = open('A-large.out', 'w')

numTests = int(inputFile.readline())


for i in range(numTests):
    line = map(lambda x: int(x), inputFile.readline().split())
    n = line[0]
    cap = line[1]
    files = map(lambda x: int(x), inputFile.readline().split())
    files.sort()
    files.reverse()
    discsNeeded = 0
    while len(files) > 1:
        if files[0] + files[-1] <= cap:
            files = files[1:-1]
        else:
            files = files[1:]
        discsNeeded += 1
    if len(files) == 1:
        discsNeeded += 1

    outputFile.write('Case #' + str(i+1) + ': ' + str(discsNeeded) + '\n')

inputFile.close()
outputFile.close()
