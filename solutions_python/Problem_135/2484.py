import sys

f = open(sys.argv[1])
testcasecount = int(f.readline())

for  testcase in range(testcasecount):
    answer1 = int(f.readline())
    cards1 = []
    for line in range(4):
        cards1.append(f.readline()[:-1].split(" "))
    answer2 = int(f.readline())
    cards2 = []
    for line in range(4):
        cards2.append(f.readline()[:-1].split(" "))

    #print("Case #%d" % (testcase+1))
    #print(answer1)
    #print(cards1)
    solutionset = cards1[answer1-1]
    #print("Must be one of: %r" % solutionset)
    #print(answer2)
    #print(cards2)
    solution = ""
    solutioncount = 0
    for cc in cards2[answer2-1]:
        if cc in solutionset:
            solution = cc
            solutioncount +=1
    if solutioncount == 0:
        print("Case #%d: Volunteer cheated!" % (testcase+1))
    elif solutioncount > 1:
        print("Case #%d: Bad magician!" % (testcase+1))
    else:
        print("Case #%d: %s" % ((testcase+1), solution))
    
