fp = open('B-large.in')
T = int(fp.readline())

for t in range(T):
    a = fp.readline().strip().split()

    c = []
    d = []
    C = int(a.pop(0))
    for i in range(C): c.append(a.pop(0))
    D = int(a.pop(0))
    for i in range(D): d.append(a.pop(0))
    N = int(a.pop(0))
    n = list(a.pop(0)) # this is our original string as a list
    ni = ''
    if len(n) < 1: print "Invalid n<1 :", n
    ni += n.pop(0)

    for i in range(len(n)):
        ni += n.pop(0)

        # combines replacements
        for ci in c:
            if (ni[-2:]==ci[0]+ci[1]) or (ni[-2:]==ci[1]+ci[0]):
                 ni = ni[:-2]+ci[2]

        # deletions
        for di in d:
            if set(di).issubset(set(ni)):
                ni = ''

    print "Case #%d:"%(t+1), str(list(ni)).replace("'","")

