from __future__ import print_function
s = """3
---+-++- 3
+++++ 4
-+-+- 4"""
s = open('A-large.in').read()
import sys
import math

ss = s.split('\n')
N = int(ss[0])

f = open('A.out', 'w')
# f = sys.stdout

for j in range(0, N):
    cs = ss[1+j].split(' ')
    c = [ch for ch in cs[0]]
    K = int(cs[1])
    flip_n = 0
    for i in range(0, len(c)-K+1):
        sym = c[i]
        if sym == '-':
            flip_n += 1
            c[i] = '+'
            for k in range(0, K-1):
                c[i + 1 + k] = '-' if c[i + 1 + k] == '+' else '+'
        # print(c)
    is_all_plus = True
    for i in range(0, len(c)):
        if c[i] == '-':
            is_all_plus = False
            break
    if is_all_plus:
        print('Case #%d: %d' % (j + 1, flip_n), file=f)
    else:
        print('Case #%d: %s' % (j + 1, 'IMPOSSIBLE'), file=f)