#!/usr/bin/python
import re
import inspect
from sys import argv, exit


def rstr():
    return input()


def rstrs(splitchar=' '):
    return [i for i in input().split(splitchar)]


def rint():
    return int(input())


def rints(splitchar=' '):
    return [int(i) for i in rstrs(splitchar)]


def varnames(obj, namespace=globals()):
    return [name for name in namespace if namespace[name] is obj]


def pvar(var, override=False):
    prnt(varnames(var), var)


def prnt(*args, override=False):
    if '-v' in argv or override:
        print(*args)


def solved(pcs):
    for pc in pcs:
        if not pc:
            return False
    return True


def get_flipped(pcs, start, length):
    flipped = [p for p in pcs]
    for i in range(start, start + length):
        flipped[i] = not flipped[i]
    return flipped

def get_num(pcs, length, limit=-1):
    if solved(pcs):
        return 0

    states = [pcs]
    n = 1
    while True:
        new_states = []
        for state in states:
            for i in range(len(pcs) - length + 1):
                new_state = get_flipped(state, i, length)
                if solved(new_state):
                    if n == limit:
                        prnt('Using limit')
                    return n
                if new_state not in states:
                    new_states.append(new_state)

        if not new_states:
            return None

        if limit != -1 and n == limit-1:
            prnt('Using limit')
            return limit

        n += 1
        prnt('{}/{}'.format(n, limit))
        states += new_states

def cut_beg(pcs):
    for i,b in enumerate(pcs):
        if not b:
            return pcs[i:], True
    return pcs, False


def pbin(li):
    prnt([1 if l else 0 for l in li])

def is_bad(pcs, length):
    n = 0
    while True:
        if solved(pcs):
            return n
        if pcs[0]:
            pcs, cut = cut_beg(pcs)
            if not cut:
                return -1
        pbin(pcs)
        if len(pcs) >= length:
            pcs = get_flipped(pcs, 0, length)
            n += 1
        else:
            return -1
        pbin(pcs)

if __name__ == '__main__':
    cases = rint()

    for i in range(cases):
        pancakes, length = rstrs()
        if pancakes[0] == '#':
            continue
        boolcakes = [True if c == '+' else False for c in pancakes]
        length = int(length)
        limit = is_bad(boolcakes, length)
        if limit == -1:
            ans = 'IMPOSSIBLE'
            prnt('\nis_bad')
        elif limit == 0:
            prnt('solved')
            ans = 0
        else:
            ans = limit
            #prnt('\nnot_is_bad')
            #ans = get_num(boolcakes, length, limit)
            #if ans is None:
            #    ans = "IMPOSSIBLE"
        print('Case #{}: {}'.format(i + 1, ans))
