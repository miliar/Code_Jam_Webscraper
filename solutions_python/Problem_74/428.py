#!/usr/bin/python3

from sys import stdin
from sys import stdout

t = int(stdin.readline())
for i in range(1, t+1):
    a = stdin.readline().split()
    n = int(a[0])
    pos = [1, 1]
    time = [0, 0]
    total = 0
    for j in range(n):
        k = (0 if a[j*2+1] == 'O' else 1)
        total = max(total+1, time[k]+abs(pos[k]-int(a[j*2+2]))+1)
        pos[k] = int(a[j*2+2])
        time[k] = total
    print('Case #{}: {}'.format(i, total))
