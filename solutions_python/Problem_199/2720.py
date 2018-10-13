import sys
import numpy as np

in_fname = sys.argv[1]

fin = open(in_fname, 'r')
T = int(fin.readline())

out_fname = in_fname.split('.')[0] + '.out'
fout = open(out_fname, 'w')

for t in xrange(1, T + 1):
    [s, k] = fin.readline().split()
    k = int(k)
    n = len(s)

    a = np.int8([x == '+' for x in s])

    c = 0
    for i in xrange(n - k + 1):
        if a[i] == 0:
            a[i : i + k] = 1 - a[i : i + k]
            c += 1

    if not a.all():
        fout.write('Case #%d: IMPOSSIBLE\n' % t)
    else:
        fout.write('Case #%d: %d\n' % (t, c))

