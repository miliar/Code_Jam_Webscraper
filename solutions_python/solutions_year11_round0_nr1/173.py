#!/usr/bin/python

def find_N(bot, case):
    for i, v in enumerate(case):
        if v[0] == bot:
            return i

    return len(case)

import sys

lines = []
with open(sys.argv[1], 'r') as FILE:
    lines = FILE.readlines()

cases = []
for line in lines[1:]:
    tmp = line.split()[1:]
    cases.append(list(zip(*([iter(tmp)] * 2))))

casenumber = 0
for case in cases:
    casenumber += 1
    secs = 0

    case = [(n, int(p)) for (n, p) in case]

    robots = sorted([{ 'next_index': find_N('B', case), 'name': 'B', 'pos': 1, 'm': False },
                     { 'next_index': find_N('O', case), 'name': 'O', 'pos': 1, 'm': False }],
                    key = lambda x: x['next_index'])

    while (case):
        secs += 1
        if case[0][1] == robots[0]['pos']:
            del(case[0])
            robots[0]['m'] = True
            if not(case): break
            for i in range(2): robots[i]['next_index'] = find_N(robots[i]['name'], case)

            robots = sorted(robots, key = lambda x: x['next_index'])

        for i in range(2):
            if not(robots[i]['m']) and (robots[i]['next_index'] < len(case)):
                nb = case[robots[i]['next_index']][1]
                if robots[i]['pos'] < nb:
                    robots[i]['pos'] += 1
                if robots[i]['pos'] > nb:
                    robots[i]['pos'] -= 1
            robots[i]['m'] = False

    print("Case #{0}: {1}".format(casenumber, secs))
