def getLines(filename):
    with open(filename) as f:
        return f.readlines()


def appendToFile(filename, text):
    with open(filename,'a') as f:
        f.write(text + '\n')


lines = getLines('A-large.in')
testsNum = int(lines[0])

for lineNum in xrange(1,testsNum + 1):
    line = lines[lineNum]
    arr = list(line.split()[1])
    counter = 0
    friends = 0
    for i in xrange(0,len(arr)):
        if i > (counter + friends):
            friends += (i - counter - friends)
        counter += int(arr[i])
    appendToFile('output.txt', "Case #"+str(lineNum) + ": " + str(friends))

