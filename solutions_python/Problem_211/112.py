__author__ = 'snv'
from heapq import heappop, heappush
from math import pi
eps = 10**(-10)
MAXVAL = 10**10


def try_fill(r, procs):
    free_volume  = sum()
# sys.setrecursionlimit(10001)

f = open('C-small-1-attempt0.in ','r')
g = open('output.txt', 'w')
T = int(f.readline())
for j in range(T):
    N, K = f.readline().split()
    N, K = int(N), int(K)
    U = float(f.readline())
    procs = sorted(list(map(float, f.readline().split())))
    procs.append(MAXVAL)

    # print(procs)


    fill_value = MAXVAL
    while U > eps:
        smallest = procs[0]
        n_smallest = 0
        for k in range (N):
            if procs[k] < smallest + eps:
                n_smallest +=1
            else:
                break
        fill_value = min (procs[n_smallest], smallest + U/n_smallest)
        # print ('try filling to level', fill_value )
        for k in range (n_smallest):
            U -= (fill_value - procs[k])
            procs[k] = fill_value

        # print ('filled', n_smallest, 'now',procs, U)

    ans = 1

    for r in range(N):
        ans *=  procs[r]
    ans_string = 'Case #{0}: {1}\n'.format(j+1, ans)
    print(ans_string)
    g.write(ans_string)
f.close()
g.close()

