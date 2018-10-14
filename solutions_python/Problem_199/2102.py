import os
import sys

lines = open(sys.argv[1]).read().strip().split('\n')
for case, l in enumerate(lines[1:]):
    s, k = l.split(' ')
    k = int(k)
    s = list(s)

    flips = 0
    for i, c in enumerate(s):
        if c == '-':
            if i + k > len(s):
                flips = -1
                break
            flips += 1
            for j in range(i, i+k):
                s[j] = '+' if s[j] == '-' else '-'
    print("Case #%d: %s" % (case+1, str(flips) if flips >= 0 else 'IMPOSSIBLE'))