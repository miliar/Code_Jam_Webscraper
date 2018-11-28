#!/usr/bin/python

from sys import stdin

def tabular(fields):
    counts = { 'X' : 0, 'O' : 0, 'T' : 0, '.' : 0}
    for field in fields:
        counts[field] += 1
    return counts

def calc(table):
    table_t = zip(*table)
    fields = []
    fields += [table[y]          for y    in range(4)]
    fields += [table_t[x]        for x    in range(4)]
    fields += [
        [table[x_y][x_y]   for x_y  in range(4)],
        [table[mx_y][3 - mx_y] for mx_y  in range(4)]
    ]
    results = map(tabular, fields)
    if max(map(lambda result: result['X'] + result['T'], results)) == 4:
        return 'X won'
    if max(map(lambda result: result['O'] + result['T'], results)) == 4:
        return 'O won'
    if max(map(lambda result: result['.'], results)) == 0:
        return 'Draw'
    return 'Game has not completed'

T = int(stdin.readline())
for i in range(T):
    table = [list(stdin.readline().strip()) for ii in range(4)]
    print "Case #%d: %s" % (i + 1, calc(table))
    stdin.readline()
