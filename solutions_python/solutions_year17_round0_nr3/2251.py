import os
from collections import defaultdict

def split(l):
    if l == 1:
        return (0, 0)
    elif l % 2:
        return ( l // 2, l //2)
    else:
        return (l // 2, l // 2 - 1)


def compute(l, p):
    gaps = [l]
    gapsd = defaultdict(int)
    gapsd[l] = 1
    for j in range(p):
        #choose first gap
        cg = gaps[0]
        tg = split(cg)
        for g in tg:
            if g in gapsd:
                gapsd[g] += 1
            else:
                gapsd[g] = 1
                gaps.append(g)
        gapsd[cg] -= 1
        if gapsd[cg] == 0:
            gaps = gaps[1:]
            gaps = sorted(gaps, reverse=True)
        #print("person {} arrived, biggest gap {}, chose {}, gaps - {}".format(j, cg, tg, gaps))
        #print(gapsd)

    return tg


#print(compute(1000, 1000))
#print(compute(1000, 1))
with open(os.sys.argv[1], 'rb') as f:
    n_of_cases = int(f.readline().strip())
    for i in range(1, n_of_cases+1):
        l, p = tuple(int(x) for x in f.readline().strip().split())
        a, b = compute(l, p)

        print("Case #{:d}: {:d} {:d}".format(i, a, b))