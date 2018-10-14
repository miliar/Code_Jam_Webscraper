#!/usr/bin/python
# vim: set fileencoding=utf-8 :

import sys

lines = [x.split() for x in sys.stdin.readlines()]

index = 1
for line in lines[1:]:
    num_combines = int(line[0])
    num_opposes = int(line[num_combines + 1])
    combines = line[1 : (num_combines + 1)]
    opposes = line[(num_combines + 2) : (num_combines + num_opposes + 2)]
    invokes = line[num_combines + num_opposes + 3]

    combine_rules = {"Q":[], "W":[], "E":[], "R":[], "A":[], "S":[], "D":[], "F":[]}
    oppose_rules = {"Q":[], "W":[], "E":[], "R":[], "A":[], "S":[], "D":[], "F":[]}
    numbers = {"Q":0, "W":0, "E":0, "R":0, "A":0, "S":0, "D":0, "F":0}
    for c in combines:
        combine_rules[c[0]].append(c[1] + c[2])
        combine_rules[c[1]].append(c[0] + c[2])
    for o in opposes:
        oppose_rules[o[0]].append(o[1])
        oppose_rules[o[1]].append(o[0])

    ret = []
    for i in invokes:
        flag = False
        if len(ret) > 0:
            for c in combine_rules[i]:
                if len(ret) > 0 and ret[-1] == c[0]:
                    numbers[ret[-1]] -= 1
                    ret[-1] = c[1]
                    flag = True
                    break
        if not flag:
            for o in oppose_rules[i]:
                if numbers[o] > 0:
                    ret = []
                    numbers = {"Q":0, "W":0, "E":0, "R":0, "A":0, "S":0, "D":0, "F":0}
                    break
            else:
                numbers[i] += 1
                ret.append(i)
    print ("Case #%d: [" + ", ".join(ret) + "]") % index
    index += 1

