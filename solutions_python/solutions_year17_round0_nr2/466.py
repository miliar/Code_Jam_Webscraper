#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# $File: solve.py
# $Date: Sat Apr 08 21:48:46 2017 +0800
# $Author: jiakai <jia.kai66@gmail.com>

def work():
    n = input().strip()
    nv = int(n)
    if int('1' * len(n)) > nv:
        return '9' * (len(n) - 1)
    ret = ''
    for idx, ch in enumerate(n):
        remain = len(n) - idx - 1
        if int(ret + ch * (len(n) - idx)) > nv:
            assert ch > '0'
            ret += str(int(ch) - 1)
            ret += '9' * (len(n) - idx - 1)
            break
        else:
            ret += ch
    brute_force_check(n, ret)
    return ret

def brute_force_check(n, to_check):
    n = int(n)
    for i in range(n, 0, -1):
        v = str(i)
        ok = True
        for idx in range(1, len(v)):
            if v[idx - 1] > v[idx]:
                ok = False
                break
        if ok:
            break

    assert v == to_check, (n, v, to_check)


def main():
    for i in range(int(input())):
        print('Case #{}: {}'.format(i + 1, work()))

if __name__ == '__main__':
    main()
