#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

input_file = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
output_file = open(sys.argv[2], 'w') if len(sys.argv) > 2 else sys.stdout

def parse(cast=None):
    line = next(input_file).split()
    return map(cast, line) if cast else line


def solve():
    '''
    一共进行了G局游戏
    今天进行了D局游戏，D<=N
    应该满足：
        Pd*D/100是整数
        Pg*G/100是整数
        今天的胜利和失败场次都小于总的胜利和失败场次
    由于总场次是不限制的，只要不是0或者100就可以接受
    '''
    N, Pd, Pg = parse(int)
    N = min(101, N + 1)
    result = "Broken"
    if (Pg == 0 and Pd != 0) or (Pg == 100 and Pd != 100):
        result = "Broken"
        D = 0
    else:
        for D in range(1, N):
            if (Pd * D) % 100 == 0:
                result = "Possible"
                break
    return result#, N, Pd, Pg, D


if __name__ == '__main__':
    from time import time

    t0 = time()

    cases = int(next(input_file))

    for case in range(1, cases + 1):
        print('Case #{case}: {result}'.
              format(case=case, result=solve()),
              file=output_file)

    print(time() - t0)


