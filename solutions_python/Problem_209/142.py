__author__ = 'snv'
from heapq import heappop, heappush
from math import pi

# sys.setrecursionlimit(10001)

f = open("A-large (1).in" ,'r')
g = open('output.txt', 'w')
T = int(f.readline())
for j in range(T):
    N, K = f.readline().split()
    N, K = int(N), int(K)
    pile_heap = []
    for pie in range(N):
        R, H = f.readline().split()
        R = int(R)
        H = int(H)
        RH = R*H
        heappush(pile_heap, (-R*R,-2*R*H))

    # print ('total', pile_heap)

    ans = 0
    for tst in range(N-K +1):
        ms = heappop(pile_heap) # square of lower
        # print (tst, 'got', ms, pile_heap, sorted([pie[1] for pie in pile_heap])[:K])
        remaining = sum(sorted([pie[1] for pie in pile_heap])[:K-1])
        ans = min(ans, ms[0] + ms[1] + remaining)

    ans =  -pi*ans
    ans_string = 'Case #{0}: {1}\n'.format(j+1, ans)
    print(ans_string)
    g.write(ans_string)
f.close()
g.close()

