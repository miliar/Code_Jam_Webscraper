#This works for the small input only (obviously)
def testCase(xominosize, bh, bw):
    if not (bh*bw)%xominosize==0:
        return "RICHARD"
    if xominosize==1:
        return "GABRIEL"
    elif xominosize==2:
        return "GABRIEL"
    elif xominosize==3:
        if (bh>=2 and bw>=3) or (bh>=3 and bw>=2):
            return "GABRIEL"
    elif xominosize==4:
        if (bh>=3 and bw>=4) or (bh>=4 and bw>=3):
            return "GABRIEL"
    return "RICHARD"

# Read the input
infile = open('D-small-attempt0.in.txt')
outfile = open('D-small-attempt0.out', 'w')
lines = infile.read().split('\n')
casecount = int(lines.pop(0))

# Solve the cases
for casenum in range(1, casecount+1):
    size, bh,bw = map(int, lines.pop(0).split())
    print >> outfile, "Case #%i: %s"%(casenum, testCase(size, bh, bw))