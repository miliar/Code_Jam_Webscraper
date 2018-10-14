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
        cases.append(int(f.readline().rstrip()))

for x in range(0, len(cases)):
    case = cases[x]
    while case > 0:
        l = [int(d) for d in str(case)]
        if all(l[i] <= l[i+1] for i in xrange(len(l)-1)):
            print("Case #" + str(x + 1) + ": " + str(case))
            break
        else:
            case -= 1
