# Case solver
def SolveCase(mushrooms):
    #Method 1
    m1_eaten = 0
    for i in range(len(mushrooms)-1):
        if mushrooms[i] > mushrooms[i+1]:
            m1_eaten += mushrooms[i]-mushrooms[i+1]
    #Method 2
    biggest_diff = 0
    for i in range(len(mushrooms)-1):
        if mushrooms[i]-mushrooms[i+1] > biggest_diff:
            biggest_diff = mushrooms[i]-mushrooms[i+1]
    m2_eaten = 0
    for i in range(len(mushrooms)-1):
        m2_eaten += min(mushrooms[i], biggest_diff)
    #Output
    return str(m1_eaten) + " " + str(m2_eaten)
    
# Run the program
if __name__=='__main__':
    infile = open('A-large.in.txt')
    outfile = open('A-large.out', 'w')
    lines = infile.read().split('\n')
    casecount = int(lines.pop(0))
    for casenum in range(1, casecount+1):
        n = lines.pop(0)
        mushrooms = map(int, lines.pop(0).split())
        print "Solving Case %i"%casenum
        print >>outfile, "Case #%i: %s"%(casenum, SolveCase(mushrooms))