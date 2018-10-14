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

flip = lambda s: ''.join('+' if c == '-' else '-' for c in s)

def run(data):
    s, k = data
    cnt = 0

    for i in range(len(s) - k + 1):
        if s[0] == '-':
            s = flip(s[1:k]) + s[k:]
            cnt += 1
        else:
            s = s[1:]

    if not all(c == '+' for c in s):
        return "IMPOSSIBLE"

    return cnt

#---------------------------------------------

def read_case():
    a = input().split()
    return (a[0], int(a[1]))

for i in range(int(input())):
    outstr = 'Case #'+str(i+1)+': '+str(run(read_case()))
    print(outstr, ' @ t =', time.clock())
    __builtins__.print(outstr)
