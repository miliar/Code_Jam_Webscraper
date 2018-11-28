#!/usr/bin/env python
import sys

def listToText(l):
    l.sort()
    return ''.join(l)

inputFile = open( 'B-large.in' )
outputFile = open( 'B-large.out', 'w' )

# testcases
t = int( inputFile.readline() )
case = 1

while case <= t:
    
    opposed = {
        'Q': set(),
        'W': set(),
        'E': set(),
        'R': set(),
        'A': set(),
        'S': set(),
        'D': set(),
        'F': set()
    }
    
    combinations = { }
    
    line = inputFile.readline().split()
    point = 0
    
    c = int(line[point])
    point += 1
    
    while point <= c: # get combinations
        combi = line[point]
        base = listToText([combi[0], combi[1]])
        combinations[base] = combi[2]
        
        point += 1
        
    d = int(line[point])
    point += 1
    
    
    while point <= c+1+d: # add opposing elements
        opp = line[point]
        opposed[opp[0]].add(opp[1])
        opposed[opp[1]].add(opp[0])
        
        point += 1
    
    n = int(line[point])
    point += 1
    summon = line[point]
    
    final = []
    cast = (x for x in summon)
    
    for spell in cast:
        if not final:
            final.append(spell)
            continue
        
        combi = listToText([final[-1], spell])
        if combi in combinations:
            final.pop()
            final.append(combinations[combi])
            continue
        
        clean = False
        for i in opposed[spell]:
            if i in final:
                clean = True
                
        if clean:
            final = []
            continue
        
        final.append(spell)
    
    outputFile.write("Case #" + str(case) + ": " + str(final).replace('\'', '') + "\n")
    case += 1

outputFile.close()
inputFile.close()