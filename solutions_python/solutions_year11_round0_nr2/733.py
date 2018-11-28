# -*- coding: utf-8 -*-

base_elements = ['Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F']
nbase_elements = ['T', 'Y', 'U', 'I', 'O', 'P', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']

T = int(raw_input())
for t in xrange(1, T+1):
    line = raw_input().split(" ")
    C = int(line[0])
    D = int(line[C+1])
    N = int(line[C+D+2])
    combineds_list = line[1:C+1] 
    opposeds_list = line[C+2:C+D+2]
    invokeds_list = list(line[C+D+3])
    combineds = {}
    opposeds = {}
    for element in base_elements:
        combineds[element] = {}
        opposeds[element] = set()
    for a, b, c in combineds_list:
        combineds[a][b] = c
        combineds[b][a] = c
    for a, b in opposeds_list:
        opposeds[a].add(b)
        opposeds[b].add(a)
    elements = []
    for element in invokeds_list:
        if len(elements) > 0:
            if elements[-1] in combineds[element]:
                elements.append(combineds[element][elements.pop()])
            elif len(set(elements) & set(opposeds[element])) > 0:
                elements = []
            else:
                elements.append(element)
        else:
            elements.append(element)
    print "Case #%d: [%s]" % (t, ", ".join(elements))
    