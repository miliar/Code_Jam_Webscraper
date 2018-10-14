def solve(cases, inFile, outputFile):
    for c in xrange(1, cases + 1):
        outputFile.write("Case #" + str(c) + ": ")
        q1 = int(inFile.readline())
        board1 = []
        for i in xrange(0, 4):
            board1.append(inFile.readline().split())
        q2 = int(inFile.readline()) 
        board2 = []
        for i in xrange(0, 4):
            board2.append(inFile.readline().split())
        row1 = board1[q1 - 1]
        row2 = board2[q2 - 1]
        matches = []
        for x in row1:
            for y in row2:
                if x == y:
                    matches.append(x)
        if len(matches) == 1:
            outputFile.write(str(matches[0]))
        elif len(matches) == 0:
            outputFile.write("Volunteer cheated!")
        else:
            outputFile.write("Bad magician!")
        outputFile.write("\n")
        
inFile = open('A-small-attempt0.in')
outputFile = open('output.txt', 'w')

cases = int(inFile.readline())
print cases, 'cases read'

solve(cases, inFile, outputFile)
print 'done'

inFile.close()
outputFile.close()