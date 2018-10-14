#!/usr/bin/python

MAX = 2
inputf = open("B-small-attempt1.in")
lines = inputf.readlines()
num = int(lines[0])
j = 1
for i in range(num):
    nm = lines[j]
    j = j + 1
    (n, m) = map(lambda x: int(x), nm.split(" "))
    t = j + n
    prog = map(lambda l: l.replace("\n", "").split(" "), lines[j:t])
    j = t
    print "Case #" + str(i + 1) + ":",
    for x, e in enumerate(prog):
        if set(e) == set(['1']):
            prog[x] = ['0'] * m
    for y in range(m):
        es = set()
        for z in range(n):
            es.add(prog[z][y])
        if len(es) == 1:
            for z in range(n):
                prog[z][y] = '0'
        elif es == set(['0', '1']) or es == set(['0', '2']):
            for z in range(n):
                prog[z][y] = '0'
    print "YES" if len(set(reduce(lambda x, y: x + y, prog, []))) == 1 else "NO"

