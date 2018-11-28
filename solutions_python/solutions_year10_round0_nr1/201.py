#!/usr/bin/python
import sys

total = int( sys.stdin.readline() )

results = []
line = 1
for case in sys.stdin.readlines():
    n, k = case.split(' ')
    n = int(n)
    k = int(k)
    state = 'ON' if (k+1) % pow(2, n) == 0 else 'OFF'
    results.append('Case #%d: %s\n' % (line, state))
    line += 1

sys.stdout.writelines(results)
