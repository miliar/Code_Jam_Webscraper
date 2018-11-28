import sys
import copy

# Get Inputs
if len(sys.argv) != 2:
    print "Incorrect number of args"
    sys.exit(-1)

# Global for cases
cases = []

# Read file in
with open(sys.argv[1], 'r') as f:
    t = int(f.readline())
    for x in range(0, t):
        cases.append(f.readline().rstrip().split(" "))
        cases[x][1] = int(cases[x][1])
        temp = cases[x][0]
        cases[x][0] = []
        for y in temp:
            if y is "+":
                cases[x][0].append(True)
            else:
                cases[x][0].append(False)


def solve(k, ck, ccases, flips):
    if all(case is True for case in ccases):
        return flips
    if ck + k > len(ccases):
        return 10000000000000  # Basically infinity
    caseOne =copy.deepcopy(ccases)
    for i in range(0, k):
        caseOne[ck+i] = not caseOne[ck+i]
    flipone = solve(k, ck + 1, caseOne, flips + 1)
    flipnone = solve(k, ck + 1, ccases, flips)
    return min(flipone, flipnone)

def solvefast(ccases, k):
    flips = 0
    for x in range(0, len(ccases) - k + 1):
        if ccases[x] is not True:
            for i in range(x, x+k):
                ccases[i] = not ccases[i]
            flips += 1
    return (ccases, flips)

# for x in range(0, t):
#     sval = solve(cases[x][1], 0, cases[x][0], 0)
#     if sval == 10000000000000:
#         print("Case #" + str(x + 1) + ": IMPOSSIBLE")
#     else:
#         print("Case #" + str(x + 1) + ": " + str(sval))

for x in range(0, t):
    sval = solvefast(cases[x][0],  cases[x][1])
    if not all(case is True for case in sval[0]):
        print("Case #" + str(x + 1) + ": IMPOSSIBLE")
    else:
        print("Case #" + str(x + 1) + ": " + str(sval[1]))