# Case solver
def SolveCase(targetn):
    n = 1
    count = 1
    while n!=targetn:
        flipped = int(str(n)[::-1])
        if n+1 < flipped <= targetn:
            testcount = 1
            for i in range(n+1, flipped):
                testflip = int(str(i)[::-1])
                if testflip <= targetn and testflip-flipped > i-(n+testcount)+1:
                    flipped = testflip
                    testcount = i-n+1
            count += testcount
            n = flipped
        else:
            n += 1
            count += 1
    return count
    
# Run the program
if __name__=='__main__':
    infile = open('A-small-attempt3.in.txt')
    outfile = open('A-small-attempt3.out', 'w')
    lines = infile.read().split('\n')
    casecount = int(lines.pop(0))
    for casenum in range(1, casecount+1):
        n = int(lines.pop(0))
        print "Solving Case %i"%casenum
        print >>outfile, "Case #%i: %i"%(casenum, SolveCase(n))