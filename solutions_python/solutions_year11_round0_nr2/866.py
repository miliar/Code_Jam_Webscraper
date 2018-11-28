#!/usr/bin/python

import re
import sys

input_file = open('B-large.in')
output_file = open('B-large.out', 'w')

T = int(input_file.readline())

def combine(invoked, combines):
    if len(invoked) < 2:
        return False
    if invoked[-1]+invoked[-2] in combines.keys():
        k = invoked.pop()+invoked.pop()
        invoked.append(combines[k])
        return True
    else:
        return False

def oppose(invoked, opposes):
    if opposes.has_key(invoked[-1]):
        for c in opposes[invoked[-1]]:
            if c in invoked[0:-1]:
                del invoked[:]


for t in range(T):
    
    
    line = input_file.readline().split(' ')
    C = int(line.pop(0))
    combines = {}
    for c in range(C):
        comb = line.pop(0)
        combines[comb[0:2]] = comb[2]
        combines[comb[1]+comb[0]] = comb[2]
#    print combines
    opposes = {}
    D = int(line.pop(0))
    for d in range(D):
        opp = line.pop(0)
        if not opposes.has_key(opp[0]):
            opposes[opp[0]] = set()
        if not opposes.has_key(opp[1]):
            opposes[opp[1]] = set()
        opposes[opp[0]].add(opp[1])
        opposes[opp[1]].add(opp[0])
        
#    print opposes
    N = int(line.pop(0))
    elements = list(line.pop(0).replace('\n', ''))
    
    invoked = []
    
    while(True):
        if len(elements) == 0:
            break
        invoked.append(elements.pop(0))
        while(combine(invoked, combines)): pass
        oppose(invoked, opposes)
        
    result = str(invoked).replace("'", "")
    output_file.write("Case #" + str(t + 1) + ": " + result + "\n")

input_file.close()
output_file.close()
