import sys

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
        cases.append(f.readline().rstrip())
        cases[x] = cases[x].split(' ')
        for q in range(0, len(cases[x])):
            cases[x][q] = int(cases[x][q])


def locate_min(a):
    smallest = min(a)
    return smallest, [index for index, element in enumerate(a) if smallest == element]

def locate_max(a):
    smallest = max(a)
    return smallest, [index for index, element in enumerate(a) if smallest == element]

casenum = 1

for case in cases:
    # Fill bathroom stalls
    # Add Guard at start

    stalls = [True]
    stallvalues = []
    # Fill middle as empty
    for x in range(0, case[0]):
        stalls.append(False)
        stallvalues.append([0,0])

    # Add Guard at end
    stalls.append(True)

    # For each person entering the bathroom
    minfinal = 0
    maxfinal = 0
    for p in range(0, case[1]):
        # For each empty stall S, compute two values LS and RS, each of which is the number of empty stalls between
        # S and the closest occupied stall to the left or right
        for x in range(1, len(stalls) - 1):
            if stalls[x] is False:
                # Find LS
                for y in list(reversed(range(0, x))):
                    if stalls[y] is True:
                        stallvalues[x - 1][0] = x - y
                        break
                # Find RS
                for y in range(x, len(stalls)):
                    if stalls[y] is True:
                        stallvalues[x - 1][1] = y - x
                        break
            else:
                stallvalues[x - 1][0] = 0
                stallvalues[x - 1][1] = 0
        # Find stalls where min(LS, RS) is maximal
        # Doing it this way because we can keep stall indicies correct
        stallsmin = []
        stallsmax = []
        for x in stallvalues:
            stallsmin.append(min(x))
        for x in stallvalues:
            stallsmax.append(max(x))
        # Locate stalls
        vals = locate_max(stallsmin)
        if type(vals[1]) is int:
            stalls[vals[1][0] + 1] = True
        else:
            maxvals = []
            maxidxs = []
            for j in vals[1]:
                maxvals.append(stallsmax[j])
                maxidxs.append(j)
            maxv = locate_max(maxvals)
            if type(maxv[1]) is int:
                stalls[maxv[1][0] + 1] = True
            else:
                # Find left most of maxes
                finalmaxidx = []
                for o in maxv[1]:
                    finalmaxidx.append(maxidxs[o])
                s = min(finalmaxidx)
                stalls[s + 1] = True
                maxfinal = stallsmax[s]
                minfinal = stallsmin[s]
    print("Case #" + str(casenum) + ": " + str(maxfinal - 1) + " " + str(minfinal - 1))
    casenum += 1
