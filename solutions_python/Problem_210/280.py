import sys
def read():
    return map(int, raw_input().strip().split())

def small(Ac, Aj):
    if len(Ac) == 2:
        a1, a2 = min(Ac), max(Ac)
        if a2[1] - a1[0] <= 720 or a2[0] - a1[1] >= 720:
            return 2
        else:
            return 4
    elif len(Aj) == 2:
        return small(Aj, Ac)
    else:
        return 2

for i in range(input()):
    nAc, nAj = read()
    Ac, Aj = [], []
    for j in range(nAc):
        Ac.append(read())
    for j in range(nAj):
        Aj.append(read())
    print "Case #{}: {}".format(i+1, small(Ac, Aj))
    print >> sys.stderr, "Case #{}: {}".format(i+1, small(Ac, Aj))
