import sys

def getline():
    return [int(x) for x in sys.stdin.readline().strip().split()]

T = getline()[0]
for testcase in range(1,1+T):
    row1 = getline()[0]
    for i in range(1,1+4):
        line = getline()
        #print "line", line
        if i == row1:
            poss = set(line)
    row2 = getline()[0]
    for i in range(1,1+4):
        line = getline()
        #print "line", line
        if i == row2:
            poss = poss.intersection(set(line))


    #print poss
    if len(poss) == 1:
        soln = list(poss)[0]
    elif len(poss) == 0:
        soln = "Volunteer cheated!"
    else:
        soln = "Bad magician!"
    print "Case #%d: %s" % (testcase, soln)
