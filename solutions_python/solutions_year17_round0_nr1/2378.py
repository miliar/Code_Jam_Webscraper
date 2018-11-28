import numpy as np

def solve(state):
    i = 0
    flips = 0
    a = state['cakes']
    k = state['k']
    while i <= a.size - k and np.any(a == 0):
        if a[i] == 0:
            a[i:i+k] = 1 - a[i:i+k]
            flips += 1
        i += 1
    if np.all(a==1):
        return flips

with open('in.txt') as f_in:
    with open('out.txt', 'w') as f_out:
        next(f_in)
        for i, line in enumerate(f_in):
            state = {}
            l = line.split()
            state['cakes'] = np.array([1 if x == '+' else 0 for x in l[0]])
            state['k'] = int(l[-1])
            res = solve(state)
            s = res if not res is None else 'IMPOSSIBLE'
            out = 'Case #%s: %s\n' %(i+1, s)
            print(out)
            f_out.write(out)
