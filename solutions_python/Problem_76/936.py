from functools import reduce
t = int(input())
for i in range(t):
    n = int(input())
    ns = list(map(int,input().split()))
    if reduce(lambda x, y: x^y, ns, 0) == 0:
        print('Case #%d: %d' % ((i+1), sum(ns)-min(ns)))
    else:
        print('Case #%d: NO' % (i+1))
