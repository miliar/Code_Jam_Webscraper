#!/usr/bin/env python
# -*- coding: utf-8 -*-


def toarray(n):
    '''
    toarray('1000') -> [0, 0, 0, 1]
    '''
    return list(reversed([int(x) for x in n]))

best = 0

def rec(values, pos, used, total, current, other):
    global best
    # caso base
    if pos == len(values):
        if len(used) == 0 or len(used) == len(values):
            return
        if current == other and total > best:
            best = total
        return

    # no utilizando el valor actual
    rec(values, pos+1, used, total, current, other)

    # utilizandolo
    used.append(pos)
    rec(values, pos+1, used, total+values[pos], current^values[pos], other^values[pos])
    used.pop()


N = int(raw_input())

for n in range(N):
    line = raw_input()
    C = int(line)

    elems = [int(x) for x in raw_input().split()]

    # comprueba si hay solucion
    value = elems[0]
    for e in elems[1:]:
        value = value ^ e


    total = 0
    best = 0

    if value != 0:
        total = 'NO'
    else:
        #elems = [toarray(bin(x).split('b')[1]) for x in elems]

        rec(elems, pos=0, used=[], total=0, current=0, other=0)
        total = best


    print 'Case #{0}: {1}'.format(n+1, total)
