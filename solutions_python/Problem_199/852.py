import sys

def map_c(x):
    if x == '+':
        return 1
    return -1

cases = [l.split() for l in open(sys.argv[1]).readlines()[1:]]
for ic, (S, K) in enumerate(cases):
    K = int(K)
    ss = [map_c(c) for c in S]
    n = len(ss)
    c = 0
    for i in range(n-K+1):
        if ss[i] == -1:
            c+=1
            for j in range(K):
                ss[i+j] = -ss[i+j]
    if -1 in ss:
        print("Case #{}: IMPOSSIBLE".format(ic+1))
    else:
        print("Case #{}: {}".format(ic+1, c))

