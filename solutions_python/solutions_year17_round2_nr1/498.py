import numpy as np

def solve(d, n , horses):
    t = 0
    for k, s in horses:
        t = max(t, (d - k) / s)
    return d/t

with open('in.txt') as f_in:
    with open('out.txt', 'w') as f_out:
        next(f_in)
        for i, line in enumerate(f_in):
            l = line[:-1].split()
            d, n = [int(x) for x in l]
            horses = []
            for _ in range(n):
                line = next(f_in)
                l = line[:-1].split()
                l = [int(x) for x in l]
                k, s = l
                horses.append([k, s])
            s = solve(d, n, horses)
            out = 'Case #%s: %s\n' %(i+1, s)
            print(out)
            f_out.write(out)
