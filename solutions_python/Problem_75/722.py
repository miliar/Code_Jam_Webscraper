import sys

def reduce_tail(e_list, comb):
    while True:
        if len(e_list) < 2:
            break

        end = "%s%s" % (e_list[-1], e_list[-2])
        if end in comb:
            e_list.pop()
            e_list.pop()
            e_list.append(comb[end])
            #print "Reducing", end, "to", comb[end]
        else:
            break

def solve(comb, opp, evoke):
    e_list = []

    for e in evoke:
        #print "Adding", e
        e_list.append(e)

        reduce_tail(e_list, comb)

        if e_list[-1] in opp and opp[e_list[-1]] in e_list:
            #print "Clearing", e_list[-1], opp[e_list[-1]]
            e_list = []


    return "[%s]" % ", ".join(e_list)
        



dataset = open(sys.argv[1])

T = int(dataset.readline())

for i in range(T):
    line = dataset.readline().split()

    COMB = {}
    OPP = {}
    EVOKE = []

    C = int(line.pop(0))
    if C > 0:
        tmp = line.pop(0)
        for j in range(C):
            idx = j * 3
            COMB["%s%s" % (tmp[idx], tmp[idx + 1])] = tmp[idx + 2]
            COMB["%s%s" % (tmp[idx + 1], tmp[idx])] = tmp[idx + 2]

    D = int(line.pop(0))
    if D > 0:
        tmp = line.pop(0)
        for j in range(D):
            idx = j * 2
            OPP[tmp[idx]] = tmp[idx + 1]
            OPP[tmp[idx + 1]] = tmp[idx]

    N = int(line.pop(0))
    if N > 0:
        EVOKE = list(line.pop(0))

    print "Case #%d: %s" % (i + 1, solve(COMB, OPP, EVOKE))


