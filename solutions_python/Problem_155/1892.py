import sys

def countFriend(maxShyLevel, peopleCounts):
    friendCount = 0
    ovationCount = peopleCounts[0]
    for shyLevel in range(1, maxShyLevel + 1):
        if peopleCounts[shyLevel] > 0 and ovationCount < shyLevel:
            friendCount += shyLevel - ovationCount
            ovationCount += friendCount
        ovationCount += peopleCounts[shyLevel]
    return friendCount
    
def main():
    inFilename = sys.argv[1]
    outFilename = sys.argv[2]

    inFile = open(inFilename, 'r')
    outFile = open(outFilename, 'w')
    line = inFile.readline().rstrip()
    testCaseCount = int(line)
    for testCase in range(1, testCaseCount + 1):
        line = inFile.readline().rstrip()
        data = line.split(' ')
        maxShyLevel = int(data[0])
        peopleCountStr = data[1]
        peopleCounts = [0] * (maxShyLevel + 1)
        for shyLevel in range(maxShyLevel + 1):
            peopleCounts[shyLevel] = int(peopleCountStr[shyLevel])
        friendCount = countFriend(maxShyLevel, peopleCounts)
        outFile.write("Case #%d: %d\n" % (testCase, friendCount))
    inFile.close()
    outFile.close()

if __name__ == '__main__':
    main()
