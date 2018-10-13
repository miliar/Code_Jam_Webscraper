import copy
# lawnmower problem

max_height = 100

def readLineOfInts(fin):
    return [int(x) for x in fin.readline().strip().split()]

def importData(filename):
    fin = open(filename)
    cases = int(fin.readline().strip())
    lawns = []
    for c in range(cases):
        dimensions = readLineOfInts(fin)
        lawns.append([])
        for j in range(dimensions[0]):
            lawns[c].append( readLineOfInts(fin))
    for l in lawns:
        for lane in l:
            print lane
        print "           break"
    return lawns

def checkLawn(lawn):
    turf = copy.deepcopy(lawn)
    for i in range(len(turf)):
        for j in range(len(turf[0])):
            turf[i][j] = max_height

    # for height...
    # mow horizontals
    # moz verticals
    for h in range(max_height-1, 0, -1):
        # print "height %s" % h
        turf = mowRows(turf, lawn, height=h)
        turf = mowCols(turf, lawn, height=h)


    print "====="
    for l in lawn:
        print l
    print "           break"
    for t in turf:
        print t
    print "------"
    # check difference
    for i in range(len(turf)):
        for j in range(len(turf[0])):
            if turf[i][j] != lawn[i][j]:
                print i, j
                return "NO"
    return "YES"

def mowRows(turf, lawn, height=1):
    for r in range(len(lawn)):
        mowRow = True
        for c in range(len(lawn[0])):
            if lawn[r][c] > height:
                mowRow = False
        if mowRow:
            # print "mowwing row: %s" % r
            for c in range(len(turf[0])):
                turf[r][c] = height
    return turf


def mowCols(turf, lawn, height=1):
    for c in range(len(lawn[0])):
        mowRow = True
        for r in range(len(lawn)):
            if lawn[r][c] > height:
                mowRow = False
        if mowRow:
            # print "mowwing col: %s" % c
            for r in range(len(turf)):
                turf[r][c] = height
    return turf


def main(lawns):
    # for each height of lawn mower
    # for each row
    # for each column
    # check if we can mow the lawn like the pattern has
    answers = []
    for l in lawns:
        answers.append(checkLawn(l))


    return answers
    

if __name__ == "__main__":
    filename = "b.in"
    filename = "B-small-attempt0.in"
    filename = "b_large_test.in"
    filename = "B-large.in"
    lawns = importData(filename)
    answers = main(lawns)
    fout = open("%s.out" % filename, 'w')
    for i in range(len(answers)):
        fout.write("Case #%s: %s\n" % (i + 1, answers[i]))
    print answers

