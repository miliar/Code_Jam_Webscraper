# usage:  (py3 a.py < a.in) > a.out

import time, sys, inspect
from itertools import combinations

lineno = lambda: inspect.currentframe().f_back.f_back.f_lineno
print = lambda *a, **k: __builtins__.print(str(lineno())+':', *a, file=sys.stderr, **k)
map = lambda *a: list(__builtins__.map(*a))
reversed = lambda *a: list(__builtins__.reversed(*a))

#---------------------------------------------

'''

'''

def find_rightmost_violation(s):
    #
    for i in range(len(s) - 1):
        if s[-i-1] < s[-i-2]:
            return i

    return None


def run(data):
    num = list(data)

    i = find_rightmost_violation(num)

    while i is not None:
        num[-i-2] = str((int(num[-i-2]) - 1) % 10)
        num[-i-1:] = (i+1) * '9'
        i = find_rightmost_violation(num)

    return int(''.join(num))

#---------------------------------------------

def read_case():
    return input()

for i in range(int(input())):
    outstr = 'Case #'+str(i+1)+': '+str(run(read_case()))
    print(outstr, ' @ t =', time.clock())
    __builtins__.print(outstr)
