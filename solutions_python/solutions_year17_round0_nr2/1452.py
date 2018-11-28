# -*- coding: utf-8 -*-

import sys
import os
import math

#input_text_path = __file__.replace('.py', '.txt')
#fd = os.open(input_text_path, os.O_RDONLY)
#os.dup2(fd, sys.stdin.fileno())

# 入力は2桁
def is_tidy(n):
    s = str(n).zfill(2)
    if s[0] <= s[1]:
        return True
    else:
        return False


def get_tidy_number(n):
    if is_tidy(n):
        return n
    else:
        while True:
            if not is_tidy(n):
                n -= 1
            if is_tidy(n):
                return n

def tidy(s, i):
    # s[i], s[i+1]からなる数値をtidyにする
    n = int(s[i] + s[i+1])
    t = get_tidy_number(n)
    t = str(t).zfill(2)
    s[i] = t[0]
    s[i+1] = t[1]
    # 後端を9で埋める
    s[i + 2:] = ['9'] * len(s[i + 2:])


def solve(N):
    """return last tidy number"""

    s = list(str(N))

    # ひとけた
    if len(s) == 1:
        return N

    # check i
    i = 0
    while True:
        num_str = s[i] + s[i+1]

        if is_tidy(num_str):
           i += 1
           if i == len(s) - 1:
               s = ''.join(s)
               return int(s)

        else:
            tidy(s, i)
            i -= 1
            if i < 0:
                if s[0] == '0':
                    # けたさがり
                    return int('9' * (len(s) - 1))
                else:
                    return int(''.join(s))



T = int(input())
f = open('submit.txt', 'w')
for i in range(T):
    N = int(input())
    answer = solve(N)
    print(N, '->', answer)
    s = 'Case #{}: {}\n'.format(i + 1, answer)
    f.write(s)
f.close()
