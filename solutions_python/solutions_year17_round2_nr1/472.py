__author__ = 'snv'
import numpy as np

f = open('A-large.in','r')
g = open('output.txt', 'w')
NC = int(f.readline())
for j in range(NC):
    d, N = list(map(int, f.readline().split()))
    print(d,N)
    mint = 0
    for i in range(N):
        k, s = list(map(int, f.readline().split()))
        t = (d-k) /s
        mint = max(t,mint)

    ans = d/mint

    ans_string = 'Case #{0}: {1}\n'.format(j+1, ans)
    print(ans_string)
    g.write(ans_string)
f.close()
g.close()

