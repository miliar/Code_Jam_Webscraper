import sys
from math import ceil


def last_tidy(n):
    for x in xrange(n, 0, -1):
        if is_tidy(x):
            return x
    return 0


def is_tidy(x):
    prev = 0
    for x in str(x):
        if prev > int(x):
            return False
        prev = int(x)
    return True


def no_decrease(x):
    prev = None
    for x in str(x):
        if prev and prev < int(x):
            return False
        prev = int(x)
    return True

filein = sys.argv[1]
with open(filein, 'r') as f:
    with open(filein.split('.')[0] + '.out', 'w') as out:
        for i, line in enumerate(f):
            if i > 0:
                out.write('Case #{}: {}\n'.format(i, last_tidy(int(line.strip()))))
