#!/usr/bin/python2

import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()

del lines[0]

n_case = 0
while lines:
    n_case += 1
    line = [int(x) for x in lines.pop(0).split()]
    L, t, N, C = line[:4]
    a = line[4:]
    spaces = (a * (N/C)) + a[:N%C]
    spaces = [2*x for x in spaces]

    initial_distance = t

    while(initial_distance and spaces):
        if spaces[0] <= initial_distance:
            initial_distance -= spaces.pop(0)
        else:
            spaces[0] -= initial_distance
            initial_distance = 0

    if not spaces:
        print "Case #%d: %d" % (n_case, t - initial_distance)
        continue

    aux_spaces = list(spaces)
    for i in range(L):
        ind = aux_spaces.index(max(aux_spaces))
        if aux_spaces[ind] == -1:
            break
        aux_spaces[ind] = -1
        spaces[ind] /= 2

    print "Case #%d: %d" % (n_case, reduce(lambda x,y:x+y,spaces) + t)
