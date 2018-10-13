import numpy as np

def clear_front_zeros(l):
    i = 0
    while l[i] == 0:
        i += 1
    return l[i:]

def solve(state):
    l = state['l']
    while not all(l[i] <= l[i+1] for i in range(len(l)-1)):
        for i in range(len(l) - 1):
            if l[i] > l[i+1]:
                l[i] -= 1
                l[i+1:] = 9
                break
        l = clear_front_zeros(l)
    return l

with open('in.txt') as f_in:
    with open('out.txt', 'w') as f_out:
        next(f_in)
        for i, line in enumerate(f_in):
            state = {}
            l = line.split()
            state['l'] = np.array([int(x) for x in line[:-1]])
            res = solve(state)
            s = ''.join([str(x) for x in res])
            out = 'Case #%s: %s\n' %(i+1, s)
            print(out)
            f_out.write(out)
