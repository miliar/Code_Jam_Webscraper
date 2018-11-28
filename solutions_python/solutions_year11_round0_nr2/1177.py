#!/usr/bin/env python
# coding: utf-8

def generate_combines(case):
    result = {}

    offset = 0

    nums = int(case[offset])
    offset += 1
    for i in range(nums):
        result[(case[offset][0], case[offset][1])] = case[offset][2]
        offset += 1

    return result

def generate_opposed(case, offset):
    result = []

    nums = int(case[offset])
    offset += 1
    for i in range(nums):
        opp = (case[offset][0], case[offset][1])
        result.append(opp)
        offset += 1

    return result

file_content = open("file").read().split("\n")

cases, data = int(file_content[0]), file_content[1:]

for i in range(cases):
    result = []

    case = data[i].split()

    c = int(case[0])
    d = int(case[c+1])
    combines = generate_combines(case)
    opposed = generate_opposed(case, c+1)
    spell = case[c+d+3]

    for j in spell:
        if len(result) > 0 and (j, result[-1]) in combines:
            value = combines[(j, result[-1])]
            result.pop()
            result.append(value)
        elif len(result) > 0 and (result[-1], j) in combines:
            value = combines[(result[-1], j)]
            result.pop()
            result.append(value)
        else:
            empty = False
            for k in result:
                if (k, j) in opposed or (j, k) in opposed:
                    result = []
                    empty = True
                    break
            if not empty:
                result.append(j)

    result = str(result)
    result = result.replace("'", "")
    print "Case #%d: %s" % (i+1, result)


