import sys
from math import sqrt, ceil
f = open(sys.argv[1], 'r')

# Number of test cases
numOfTests = int(f.readline())

for i in range(1, numOfTests + 1) :
    print "Case #" + str(i) + ":",

    # Read test case
    testCase = f.readline().split(' ')
    n = int(testCase[0])
    m = int(testCase[1])

    pattern = []
    for i in range(n) :
        row = []
        for j in f.readline().split(' ') :
            row.append(int(j))
        pattern.append(row)

    # Check test case
    oneColumns = set()
    for i in range(n) :
        rowSum = 0
        oneColumnsTemp = set()
        for j in range(m) :
            rowSum += pattern[i][j]
            if pattern[i][j] == 1 :
                oneColumnsTemp.add(j)
        if rowSum != m :
            oneColumns = oneColumns | oneColumnsTemp

    ans = "YES"
    for j in oneColumns :
        for i in range(n) :
            if pattern[i][j] == 2 :
                ans = "NO"
                break
        if ans == "NO" :
            break
    print ans
