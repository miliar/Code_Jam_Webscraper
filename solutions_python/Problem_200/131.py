# -------------------------
# Google Code Jam 2017
# Qualification Round
# 2017 April 7
# Brendan Wood
# brendanwood1989@gmail.com
# -------------------------

filename = 'B-large'

def solve(N):
    S = str(N)
    L = len(S)
    for d in range(L):
        if int(S[d]*(L-d)) <= int(S[d:]):
            continue
        else:
            return int(S[:d] + str(int(S[d])-1) + '9'*(L-d-1))
    return int(S)
    
with open(filename+'.in') as f:
    data = f.read().splitlines()

f = open(filename+'.out', 'w')

T = int(data.pop(0))

for case in range(T):
    N = int(data.pop(0))
    f.write('Case #{}: {}\n'.format(case+1,solve(N)))
        
f.close()
