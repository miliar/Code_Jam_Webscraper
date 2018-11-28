# -*- coding: utf-8 -*-

import sys
import os

input_text_path = __file__.replace('.py', '.txt')
fd = os.open(input_text_path, os.O_RDONLY)
os.dup2(fd, sys.stdin.fileno())

T = int(input())

f = open('submit.txt', 'w')
for t in range(T):
    D, N = map(int, input().split())
    max_time = 0
    for n in range(N):
        pos, speed = map(int, input().split())
        need_time = (D - pos) / speed
        if need_time > max_time:
            max_time = need_time
    my_speed = D / max_time
    s = 'Case #{}: {:.6f}'.format(t+1, my_speed)
    print(s)
    f.write(s + '\n')
f.close()