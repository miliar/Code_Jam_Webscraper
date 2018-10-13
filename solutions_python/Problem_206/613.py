
from collections import defaultdict

def do():
    d,n = map(int, input().split())

    H = [[int(x) for x in input().split()] for _ in range(n)]

    F = []
    for k,s in H:
        F.append((d-k)/s)
    t = max(F)

    minv = d/t
    print('%.10f' % (minv))

t = int(input())

for _ in range(t):
    print('Case #%d: '%(_+1), end='')
    do()






