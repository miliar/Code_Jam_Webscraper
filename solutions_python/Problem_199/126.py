# -------------------------
# Google Code Jam 2017
# Qualification Round
# 2017 April 7
# Brendan Wood
# brendanwood1989@gmail.com
# -------------------------

filename = 'A-large'

def flip(old,K):
    new = ''
    for k in range(K):
        if   old[k] == '-':
            new += '+'
        elif old[k] == '+':
            new += '-'
    new += old[K:]
    return new

def solve(S,K):
    flips = 0
    while True:
        i = S.find('-')
        if i == -1:
            return flips
        else:
            S = S[i:]
            if len(S) < K:
                return 'IMPOSSIBLE'
            S = flip(S,K)
            flips += 1
    
with open(filename+'.in') as f:
    data = f.read().splitlines()

f = open(filename+'.out', 'w')

T = int(data.pop(0))

for case in range(T):
    S,K = data.pop(0).split(' ')
    K = int(K)
    f.write('Case #{}: {}\n'.format(case+1,solve(S,K)))
        
f.close()
