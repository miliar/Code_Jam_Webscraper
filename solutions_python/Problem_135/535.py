import sys

with open(sys.argv[-1], 'r') as infile:
    numcases = int(infile.readline().strip())

    for x in range(0, numcases):
        row = int(infile.readline().strip()) - 1
        for y in range(0, row):
            infile.readline()
        rowrow = {int(item) for item in infile.readline().strip().split(' ')}
        for y in range(0, 3-row):
            infile.readline()
        
        row = int(infile.readline().strip()) - 1
        for y in range(0, row):
            infile.readline()
        rowrow2 = {int(item) for item in infile.readline().strip().split(' ')}
        for y in range(0, 3-row):
            infile.readline()

        intersect = rowrow2.intersection(rowrow)

        res = len(intersect)

        if res == 1:
            print "Case #%d: %d" % (x+1, intersect.pop())
        elif res == 0:
            print "Case #%d: Volunteer cheated!" % (x+1)
        else:
            print "Case #%d: Bad magician!" % (x+1)
