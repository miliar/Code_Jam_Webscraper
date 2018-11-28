#!/usr/bin/env python3

import os
import sys

def is_tidy(n):
    perv_i = int(str(n)[-1])
    for i in list(reversed(str(n)[:-1])):
        if perv_i < int(i):
            return False
        else:
            perv_i = int(i)
    return True


def main():
    T = int(input())
    for i in range(T):
        N, K = input().split()
        N = int(N)
        K = int(K)
        stalls_list = [N]
        for p in range(K):
            # print(stalls_list)
            max_batch = max(stalls_list)
            stalls_list.remove(max_batch)

            if max_batch % 2 == 0:
                ls = int((max_batch / 2) - 1)
                rs = int(max_batch / 2)
                stalls_list.append(ls)
                stalls_list.append(rs)

            else :
                ls = rs = int(max_batch // 2)
                stalls_list.append(ls)
                stalls_list.append(rs)

            if p == K - 1:
                max_lr = max(ls,rs)
                min_lr = min(ls, rs)



        print('Case #{}: {} {}'.format(i + 1, max_lr, min_lr))


if __name__ == '__main__':
    main()
