#-*-coding:utf-8-*-

import os, sys, re, math


def is_happy(value, base, visited=None):
    if visited is None: visited = set([])
    #print('check {0}'.format(value))
    numbers = []
    while value > 0:
        r = value % base
        numbers.append(r)
        value = int(value / base)
        pass
    #print(numbers)
    s = sum([x ** 2 for x in numbers])
    if s == 1:
        return True
    if s in visited:
        return False
    visited.add(s)
    #if s > base:
    return is_happy(s, base, visited)

#print(is_happy(82, 3, set([82, ])))
    
#def find(bases):

happy_cache = {}

def find_happy(bases):
    n = 2
    for b in bases:
        if b in happy_cache:
            if happy_cache[b] > n:
                n = happy_cache[b]
                pass
            pass
        else:
            i = 2
            while 1:
                if is_happy(i, b):
                    happy_cache[b] = i
                    if i > n:
                        n = i
                        pass
                    break
                i += 1
                pass
            pass
        pass
    while 1:
        flag_all = True
        for b in bases: 
            if is_happy(n, b) is False:
                flag_all = False
                break
            pass
        if flag_all:
            break
        n += 1
        pass
    return n

#print(find_happy([9,10]))

fh = open(sys.argv[1])
N = int(fh.readline())
for cn in range(1, N + 1):
    numbers = map(int, fh.readline().split(' '))
    n = find_happy(numbers)
    print("Case #{0}: {1}".format(cn, n))
    pass
