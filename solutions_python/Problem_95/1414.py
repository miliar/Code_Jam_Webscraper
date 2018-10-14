f1, f2 = [open(s) for s in ["01", "02"]]
D = {}
for x, y in zip(f1.read(), f2.read()):
    D[x] = y;
from sys import stderr
F = [(D[x], x) for x in D]
F = sorted(F)
D['z'] = 'q'
D['q'] = 'z'
print('\n'.join(map(str, F)), file=stderr)
from sys import argv
f = open(argv[1])
L = f.readlines()
n = int(L[0])
for i in range(1, n + 1):
    print('Case #' + str(i) + ': ' + ''.join(D[x] for x in L[i]), end='')
