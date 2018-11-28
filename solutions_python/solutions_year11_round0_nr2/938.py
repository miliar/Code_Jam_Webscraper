import math
import sys

infile = open('test.in', 'r')
cases = int(infile.readline().strip())

for case in range(cases):
    line = infile.readline().strip().split()
    it = iter(line)

    combination = dict()
    combines = int(next(it))
    for combine in range(combines):
        temp = next(it)
        key = (temp[0], temp[1]) if temp[0] < temp[1] else (temp[1], temp[0])
        combination[key] = temp[2]

    opposition = list()
    opposes = int(next(it))
    for oppose in range(opposes):
        temp = next(it)
        opposition.append((temp[0], temp[1]) if temp[0] < temp[1] else (temp[1], temp[0]))

    next(it) #skip N
    elements = next(it)

    existing = []
    for element in elements:
        if len(existing) == 0:
            existing.append(element)
            continue
        action = False
        key = (element, existing[-1]) if element < existing[-1] else (existing[-1], element)
        if key in combination:
            existing.pop()
            existing.append(combination[key])
            continue
        for exist in existing:
            key = (element, exist) if element < exist else (exist, element)
            if key in opposition:
                existing = []
                action = True
                break
        if not action:
            existing.append(element)
            
    output = ', '.join(existing)
    print "Case #{0}: [{1}]".format(case+1, output)
