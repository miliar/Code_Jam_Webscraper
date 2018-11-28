#! /usr/bin/env python
import sys

for test_case in range(int(sys.stdin.readline().strip())):
    line = sys.stdin.readline().strip().split(" ")
    
    i = 0
    start = 0

    C = int(line[i])
    i += 1
    start = i
    combinations = []
    while i < (start + C):
        combinations.append(line[i])
        i += 1
    
    D = int(line[i])
    i += 1
    start = i
    oppositions = []
    while i < (start + D):
        oppositions.append(line[i])
        i += 1
        
    to_invoke = line[-1]
        
    combination_table = {}
    for combination in combinations:
        combination_table[combination[0],combination[1]] = combination[2]
        combination_table[combination[1],combination[0]] = combination[2]    
    def combine(elements):
        if len(elements) < 2:
            return
            
        (left, right) = elements[-2:]
        if (left,right) in combination_table:
            elements[-2:] = [combination_table[(left,right)]]
    
    opposition_table = {}
    for opposition in oppositions:
        opposition_table[opposition[0]] = opposition[1]
    def oppose(elements):
        as_set = set(elements)
        for k in opposition_table:
            if k in as_set and opposition_table[k] in as_set:
                elements[0:] = []
                return
    
    output = []
    for e in to_invoke:
        output += e
        
        combine(output)
        oppose(output)
        
    print "Case #%s: %s" % (test_case + 1, str(output).replace("'", ""))
