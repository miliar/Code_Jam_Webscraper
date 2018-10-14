import psyco
psyco.full()

import sys
import itertools
import copy

infile = open(sys.argv[1])

try:
    outfile = open(sys.argv[2], 'w')
    
except IndexError:
    outfile = sys.stdout
    
lines = infile.readlines()

num_candies = 0

def patricks_value(l):
    
    ret = l[0]
    
    for value in l[1:]:
        ret = ret ^ value
        
    return ret

def powerset(iter):
    
    s = list(iter)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s) + 1))

def flatten(iter):
    return itertools.chain.from_iterable(iter)

for index, line in enumerate(lines):
    
    if index == 0:
        continue
    
    if (index + 1) % 2 == 0:
        
        num_candies = int(line)
        continue
                
    candy_values = map(int, line.split())
    best_pile = []
        
    for possible_pile in filter(None, powerset(enumerate(candy_values))):
        
        seans_pile = []
        patricks_pile = copy.copy(candy_values)
        
        for idx, value in possible_pile:
            
            seans_pile.append(value)
            patricks_pile[idx] = 0
            
        if patricks_value(seans_pile) == patricks_value(patricks_pile) and patricks_pile != [0] * len(patricks_pile):
            
            if sum(seans_pile) > sum(best_pile):
                best_pile = list(seans_pile)
    
    if len(best_pile) == 0:
        result = 'NO'
        
    else:
        result = sum(best_pile)
        
    print >> outfile, 'Case #%d:' % (index % 2 == 0 and (index / 2) or ((index + 1) / 2)), result