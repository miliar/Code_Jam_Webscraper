import sys

def solve(fname):
    infile = open(fname, 'rb')
    outfile = open("QA_solution.txt", 'wb')

    lines = infile.readlines()
    ntests = int(lines[0].strip())

    testlength = 10
    
    def getrows(test):
        zeroindex = 1+testlength*test
        rownumA = int(lines[zeroindex].strip())
        rowA = [int(x) for x in lines[zeroindex + rownumA].strip().split(' ')]
        rownumB = int(lines[zeroindex + testlength/2].strip())
        rowB = [int(x) for x in lines[zeroindex + testlength/2 + rownumB].strip().split(' ')]
        return (rowA,rowB)

    
    for test in range(ntests):
        row1, row2 = getrows(test)
        intersects = set(row1) & set(row2)
        if len(intersects) == 0:
            outfile.write("Case #%d: Volunteer cheated!\n" %(test+1))
        elif len(intersects) == 1:
            outfile.write("Case #%d: %d\n" %(test + 1, intersects.pop()))
        else:
            outfile.write("Case #%d: Bad magician!\n" %(test+1))


            
solve(sys.argv[1])
