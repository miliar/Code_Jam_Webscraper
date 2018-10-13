# Has been a great while since I coded...Here Goes
# Snapper
# Usage pretty simple: Q1.py <inputfile>
# requires a EOF to terminate


#Read Input - Absolutely 0 input checks

import fileinput

    
infile = fileinput.input()

p = infile.readline()

T = long(p)

t = 0


while t < T:
    t += 1
    params = infile.readline()
    N = long(params)

    wires = []
    inter = 0
    for n in range(0,N):    
        params = infile.readline()
        wires.append([long(p) for p in params.split()])

    for n in range(0,N):
        for k in range(n+1,N):
            if wires[n][0] > wires[k][0] and wires[n][1] < wires[k][1]:
                inter += 1
            elif wires[n][0] < wires[k][0] and wires[n][1] > wires[k][1]:
                inter += 1

    print 'Case #%d: %d' % (t, inter)

infile.close()

