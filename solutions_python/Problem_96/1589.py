#! /usr/bin/env python

import sys, os, math

f = file(sys.argv[1])
lines = f.readlines()
f.close()

inputData = []
T = int(lines[0].strip())

pos = 1
for c in range(T):
    inputData.append( map(int, lines[pos].strip().split()) )
    pos = pos + 1

def analyse(data):
    N = data[0]
    S = data[1] #suprising triplets
    p = data[2] #maximum participants above this peformance
    t_vals = data[3:]
    count = 0
    for t in t_vals:
        if math.ceil(t/3.0) >= p:
            count = count + 1
        elif S > 0 and math.ceil(t/3.0) +1 >= p and t >= 2 and t % 3 <> 1 :
            S = S - 1
            count = count + 1 
    return count

output = []
for case,input in enumerate(inputData):
    print('case %i : inputs %s' % (case+1, input))
    res = analyse(input)
    output.append('Case #%i: %s' % (case+1, res))
    print(output[-1])

f = file(sys.argv[1].replace('.in','.out'),'w')
f.write('\n'.join(output))
f.close()
