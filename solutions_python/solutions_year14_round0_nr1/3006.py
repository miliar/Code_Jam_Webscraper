fh = open("A-small-attempt0.in", "r")
fh2 = open("magictrickoutput.txt", "w")
testCases = fh.readline()

for i in xrange(int(testCases)):
    index1 = fh.readline()
    grid1 = [[], [], [], []]
    
    for j in xrange(4):
        nextline = fh.readline()
        for k in xrange(3):
            grid1[j] += [int(nextline[0: nextline.index(" ")])]
            nextline = nextline[nextline.index(" ") + 1:]
        grid1[j] += [int(nextline)]

    index2 = fh.readline()
    grid2 = [[], [], [], []]
    
    for j in xrange(4):
        nextline = fh.readline()
        for k in xrange(3):
            grid2[j] += [int(nextline[0: nextline.index(" ")])]
            nextline = nextline[nextline.index(" ") + 1:]
        grid2[j] += [int(nextline)]

    intersection = list(set(grid1[int(index1) - 1]) & set(grid2[int(index2) - 1]))

    if len(intersection) == 0:
        fh2.write("Case #" + str((i + 1)) + ": Volunteer cheated!\n")
    if len(intersection) == 1:
        fh2.write("Case #" + str((i + 1)) + ": " + str(intersection[0]) + "\n")
    if len(intersection) > 1:
        fh2.write("Case #" + str((i + 1)) + ": Bad magician!\n")

fh.close()
fh2.close()
    
    
    
        
