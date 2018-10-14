from __future__ import print_function, division
from math import ceil, floor

import numpy as np
# Fernando Gonzalez del Cueto. Code Jam 2017

#infile = 'test2.in'
infile = 'B-small-attempt2.in'
outfile = infile.replace('.in', '.out')

fid = open(infile, 'r')

n_cases = int(fid.readline().strip())

f_out = open(outfile, 'w')

def solver(rata_q, p):

    assert isinstance(rata_q, np.ndarray)
    assert isinstance(p, np.ndarray)
    n_ingredients, n_packages = p.shape

    taken = np.zeros_like(p, dtype=bool)

    lb = int(floor(np.min(np.min(0.9*p / rata_q, axis=1))))
    ub = int(ceil(np.max(np.max(1.1*p / rata_q, axis=1))))

    kits = 0

    for q in range(lb, ub+1):

        if (p==0).all():
            return kits

        t = (p >= rata_q * (q * 0.9)) & (p <= rata_q * (q * 1.1))
        can_make = t.astype(np.uint8).sum(axis=1)
        max_kits = can_make.min()
        if max_kits.min() > 0:

            kits += max_kits
            if test_case==88:
                pass
            for row in range(p.shape[0]):
                eliminated = 0
                for col in range(p.shape[1]):
                    if t[row,col]:
                        p[row,col] = 0 # used, take them out
                        eliminated += 1
                        if eliminated >= max_kits:
                            break

    return kits

for test_case in range(1,n_cases+1):

    n_ingredients, n_packages = map(int, fid.readline().strip().split())
    rata_q = map(int, fid.readline().strip().split())
    r = np.array(rata_q).reshape((n_ingredients,1))
    l = []
    for i_ing in range(n_ingredients):
        l.append(map(int, fid.readline().strip().split()))
    a = np.array(l, dtype=np.float64)

    print('Case %i' % test_case)
    print(n_ingredients, n_packages)
    print(rata_q)
    print(a)
    if test_case == 5:
        pass
    sol = solver(r, a)

    print(sol)

    l = 'Case #%i: %i\n' % (test_case, sol)
    print(l)
    f_out.write(l)

f_out.close()