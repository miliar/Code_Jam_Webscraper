__author__ = 'snv'
import numpy as np

f = open('B-small-attempt1.in','r')
g = open('output.txt', 'w')
NC = int(f.readline())
colors = 'ROYGBV'
for j in range(NC):
    horses= list(map(int, f.readline().split()))
    N = horses[0]
    horses = np.array(horses[1:])
    ro = horses.argsort()[::-1]
    ans = ['.']*N
    if max(horses)>N//2:
        ans = 'IMPOSSIBLE'
    else:
        c = ''
        for i in range(6):
            c+= colors[ro[i]]* horses[ro[i]]
        for i in range(N):
            pos = (i*2) % N
            if ans[pos] !='.':
                pos+=1
                pos = pos % N
            ans[pos] = c[i]


    ans_string = 'Case #{0}: {1}\n'.format(j+1, "".join(ans))
    print(ans_string)
    g.write(ans_string)
f.close()
g.close()

