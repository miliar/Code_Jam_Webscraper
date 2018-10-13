#! /usr/bin/python

import sys, os

f = file(sys.argv[1])
lines = f.readlines()
f.close()

inputData = []
cases = int(lines[0].strip())

pos = 1
for case in range(cases):
    N, L, H = map(int, lines[pos].strip().split())
    freq =  map(int, lines[pos+1].strip().split())
    inputData.append( [ N, L, H, freq ] )
    pos = pos + 2

def in_harmony(a,b):
    if a < b:
        return (b/a) == (1.0 * b /a)
    else:
        return (a/b) == (1.0 * a /b)

def analyse(data):
    N, L, H, freq = data
    print('N, L, H, freq',N, L, H, freq)

    for i in range(L, H+1):
        valid = True
        for j,f in enumerate(freq):
            if not in_harmony(i,f):
                valid = False
                break
        if valid:
            return i
    return 'NO'


output = []
for case,input in enumerate(inputData):
    res = analyse(input)
    output.append('Case #%i: %s' % (case+1, res))
    print(output[-1])

f = file(sys.argv[1].replace('.in','.out'),'w')
f.write('\n'.join(output))
f.close()
