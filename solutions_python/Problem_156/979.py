import operator

try:
    input = raw_input
except:
    pass

def soluce(p):
    t_min = max(p)
    mi = [i for i, j in enumerate(p) if j == t_min]
    if t_min <= 3:
        return t_min
    #sd = set()
    for c in range(t_min // 2 + 1, 1, -1):
        #if c != 1:
        #    for done in sd:
        #        if done % c == 0:
        #            continue
        #sd.add(c)
        np = p[:]
        for i in mi:
            np.append(c)
            np[i] -= c
        t_min = min(t_min, soluce(np) + len(mi))
    return t_min


T = int(input())

for i in range(T):
    input()
    p = list(map(int, input().split()))
    s = soluce(p)
    print('Case #{}: {}'.format(i + 1, s))
