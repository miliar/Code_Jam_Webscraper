#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import izip_longest

def grouper(n, iterable, fillvalue=None):
    '''
    Copied from python doc: http://docs.python.org/library/itertools.html

    grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx

    grouper(2, 'O 2 B 1 B 2 0 4'.split()) ->
        ('O', '2'), ('B', '1'), ('B', '2'), ('O', '4')
    '''

    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)


N = int(raw_input())

for n in range(N):
    line = raw_input().split()
    elems = int(line[0])

    b_pos = 1
    b_time = 0
    o_pos = 1
    o_time = 0
   
    total = 0
    for who, goal in grouper(2, line[1:]):
        goal = int(goal)

        if who == 'O':
            # turnos que ha estado sin hacer nada
            spare = total - o_time
            # distancia desde la posicion actual al objetivo
            dist = abs(goal - o_pos)
            # coste de ir al boton aprovechando los turnos libres
            cost = max(0, dist - spare)
            total += cost + 1 

            o_pos = goal
            o_time = total

        elif who == 'B':
            # igual que con O pero cambiando los nombres de variables
            spare = total - b_time
            dist = abs(goal - b_pos)
            cost = max(0, dist - spare)
            total += cost + 1

            b_pos = goal
            b_time = total

        else:
            raise NotImplemented

    print 'Case #{0}: {1}'.format(n+1, total)
