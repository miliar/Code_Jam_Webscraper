from sys import argv

def do_case(numCase, inputFile, outputFile):
    case = inputFile.readline()
    smax, audience = case.split()

    standing = 0
    totalFriends = 0
    for i,n in enumerate(audience):
        if i >= standing:
            newFriends = i - standing
            totalFriends += newFriends
            standing += newFriends
        standing += int(n)
    print smax, audience, totalFriends
    outputFile.write("Case #{}: {}\n".format(numCase, totalFriends))

if __name__ == '__main__':
    if len(argv) != 2:
        print "Usage: $> python2.7 {} INPUT_FILE".format(argv[0])
    else:
        inputFile = open(argv[1])
        outputFile = open('output.txt', 'w')

        numCases = int(inputFile.readline())

        for case in range(numCases):
            do_case(case+1, inputFile, outputFile)
