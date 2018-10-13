#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_array():
    return [list(input()) for _ in range(4)]

def test(s):
    if 'X' in s and s <= {'X', 'T'}:
        return 'X'
    elif 'O' in s and s <= {'O', 'T'}:
        return 'O'
    else: return None 

def check(a):
    for l in a:
        s = set(l)
        c = test(s)
        if c in ['O', 'X']:
            return c + ' won'
    for i in range(4):
        s = set([l[i] for l in a])
        c = test(s)
        if c in ['O', 'X']:
            return c + ' won'
    s = set([a[i][i] for i in range(4)])
    c = test(s)
    if c in ['O', 'X']:
        return c + ' won'
    s = set([a[i][3-i] for i in range(4)])
    c = test(s)
    if c in ['O', 'X']:
        return c + ' won'
    if '.' in set(sum([l for l in a], [])):
        return 'Game has not completed'
    return 'Draw'

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        a = get_array()
        print('Case #{}: {}'.format(i+1, check(a)))
        try:
            input()
        except:
            break
