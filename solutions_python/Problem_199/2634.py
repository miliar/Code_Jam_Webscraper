import os
def solve(p, w):
    p = list( True if x == '+' else False for x in p)
    c, i, n  = 0, 0, len(p)
    possible = True
    while i < n:
        if not p[i]:
            if i + w <=n:
                c += 1
                for j in range(w):
                    p[i+j] = not p[i+j]
            else:
                return -1
        i += 1
    return c

with open(os.sys.argv[1], 'rb') as f:
    n_of_cases = int(f.readline().strip())
    for i in range(1, n_of_cases+1):
        tmp = list(f.readline().strip().split())
        p = list(tmp[0])
        w = int(tmp[1])
        r = solve(p, w)
        if r >=0:
            print("Case #{:d}: {:d}".format(i, r))
        else:
            print("Case #{:d}: IMPOSSIBLE".format(i))
