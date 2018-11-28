import sys

def sol(l):
    total = 0
    maxv = 0
    second = 0
    for i in range(1, len(l)):
        if l[i] < l[i-1]:
            maxv = max(l[i-1] - l[i], maxv)
            total += l[i-1] - l[i]
    for i in range(len(l) - 1) :
        if l[i] < maxv:
            second += l[i]
        else:
            second += maxv
    return total, second


casenum = int(sys.stdin.readline())

testcases = []

for i in range(casenum):
    length = int(sys.stdin.readline())
    line = sys.stdin.readline()
    case = []
    for i in line.split():
        case.append(int(i))
    testcases.append(case)


caseno = 1

for testcase in testcases:
    first , second = sol(testcase)
    print "Case #" + str(caseno) + ":", first, second
    caseno += 1
