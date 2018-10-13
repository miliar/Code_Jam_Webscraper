# -------------------------
# Google Code Jam 2017
# Qualification Round
# 2017 April 8
# Brendan Wood
# brendanwood1989@gmail.com
# -------------------------
filename = 'C-large'

from collections import Counter

def solve(N,K):
    c = Counter()
    c[N] = 1
    
    
    M = max(c.keys())
        
    while K > c[M]:
        K -= c[M]
        # split largest group into smaller groups
        if M % 2:  # odd
            c[(M-1)//2] += 2*c[M]
        else:  # even
            c[M//2] += c[M]
            c[M//2-1] += c[M]
        del c[M]
        # remove keys with value of zero
        c += Counter()
        M = max(c.keys())

    if M % 2:  # odd
        y = (M-1)//2
        z = (M-1)//2
    else:  # even
        y = M//2
        z = M//2-1
        
    return (y,z)
    
with open(filename+'.in') as f:
    data = f.read().splitlines()

f = open(filename+'.out', 'w')

T = int(data.pop(0))

for case in range(T):
    N,K = map(int,data.pop(0).split())
    y,z = solve(N,K)
    f.write('Case #{}: {} {}\n'.format(case+1,y,z))
        
f.close()