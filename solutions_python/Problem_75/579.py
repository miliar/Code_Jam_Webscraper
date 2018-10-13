#!/usr/bin/env python2.7
import sys
import itertools
import collections

def solve(combinations, oppositions, input_elements):
    current = []
    current_counts = collections.Counter()
    
    for element in input_elements:
        if not current:
            current.append(element)
            current_counts[element] += 1
        else:
            latest = current[-1]
            last_two = frozenset((latest, element))
            
            if last_two in combinations:
                current_counts.subtract(latest)
                current_counts[combinations[last_two]] += 1
                current[-1] = combinations[last_two]
            else:
                current.append(element)
                current_counts[element] += 1
            
            for opposition in oppositions:
                if opposition.issubset(frozenset(current_counts)):
                    del current[:]
                    current_counts.clear()
            
            for item in list(current_counts):
                if not current_counts[item]:
                    del current_counts[item]
                
    return "[{0}]".format(", ".join(current))

def parse_line(line):
    parts = collections.deque(line.strip().split())
    
    combinations = dict()
    oppositions = set()
    
    n_combinations = int(parts.popleft())
    
    for _ in range(n_combinations):
        in_a, in_b, result = parts.popleft()
        combinations[frozenset((in_a, in_b))] = result
    
    n_oppositions = int(parts.popleft())
    
    for _ in range(n_oppositions):
        oppositions.add(frozenset(parts.popleft()))
    
    input_length = parts.popleft()
    
    return combinations, oppositions, list(parts.popleft())

for n, line in enumerate(sys.stdin):
    if n == 0:
        continue # number of cases
    
    result = solve(*parse_line(line))
    
    print "Case #{0}:".format(n), result
    
