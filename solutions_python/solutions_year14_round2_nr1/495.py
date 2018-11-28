#!/usr/env/python

from sys import stdin

def parse_line():
    raw = stdin.readline().strip()
    char = None
    count = 0
    line = []
    for cur in raw:
        if cur == char:
            count +=1
            continue
        elif cur is not None:
            line.append((char, count))
        count = 1
        char = cur
    if cur is not None:
        line.append((char, count))
    return line

def parse_prob():
    nb_input = int(stdin.readline().strip())
    table = []
    for i in range(0,nb_input):
        table.append(parse_line())
    leng = len(table[0])
    for i in range(1,nb_input):
        if len(table[i]) != leng:
            return -1
    c = 0
    for j in range(leng):
        char = table[0][j][0]
        for i in range(1,nb_input):
            if table[i][j][0] != char:
                return -1
        total = sum([line[j][1] for line in table])
        moy = int(round(total / float(nb_input)))
        c += sum([abs(line[j][1] - moy) for line in table])
    return c

def solve_prob():
    val = parse_prob()
    if val < 0:
        return 'Fegla Won'
    else:
        return str(val)


nb = int(stdin.readline().strip())
for i in range(1, nb + 1):
    print('Case #{}: {}'.format(i, solve_prob()))
