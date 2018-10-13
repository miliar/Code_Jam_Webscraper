#!/usr/bin/env python
import sys

f = sys.stdin
n = int(f.readline())

for case in range(1, n + 1):
    n = f.readline().strip()
    while n[0] == '0':
        n = n[1:]
    if len(n) == 1:
        next = n + '0'
    else:
        for i in range(len(n) - 2, -1, -1):
            if n[i] < n[i+1]:
                for j in range(len(n) - 1, -1, -1):
                    if n[j] > n[i]:
                        next = list(n)
                        next[i], next[j] = n[j], n[i]
                        next = next[:i+1] + list(reversed(next[i+1:]))
                        next = ''.join(next)
                        break
                else:
                    raise Exception('Grrr!')
                break
        else:
            next = sorted(n)
            next = [next[0], '0'] + next[1:]
            next = ''.join(next)
    if next[0] == '0':
        next = ''.join(sorted(next))
        minv = min(next.replace('0', ''))
        p = next.rfind(minv)
        next = next[p] + next[:p] + next[p+1:]
    print 'Case #%i: %s' % (case, next)
