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


def adjust_stalls(stalls, key, amt):
    if stalls[key] == amt:
        del stalls[key]
    else:
        stalls[key] -= amt
    return stalls


def get_sol(s, people):
    stalls = {s: 1}
    while people > 0:
        z = max(stalls.keys())
        amt = min(people, stalls[z])
        assert amt != 0
        people -= amt
        stalls = adjust_stalls(stalls, z, amt)

        z -= 1
        if z % 2 == 0:
            nums = [z // 2, z // 2]
        else:
            nums = [z // 2, z // 2 + 1]

        for num in nums:
            if num == 0:
                continue
            if num in stalls.keys():
                stalls[num] += amt
            else:
                stalls[num] = amt
    return max(nums), min(nums)


if __name__ == '__main__':
    n = rint()
    for i in range(n):
        stalls, people = rints()
        y, z = get_sol(stalls, people)
        print('Case #{}: {} {}'.format(i + 1, y, z))
