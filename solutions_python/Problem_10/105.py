# -*- coding: utf-8 -*-
f = open('input', 'r')
lines = f.readlines()
#skip the first line
N = int(lines[0])
for i in range(N):
    t = lines[2*i+1].split()
    perKey = int(t[0])
    keys = int(t[1])
    let = int(t[2])
    if let > perKey*keys:
        print 'Case #%s: Impossible' % i+1
        continue
    t = lines[2*(i+1)].split()
    freq = []
    for f in t:
        freq.append(int(f))
    freq.sort(reverse=True)
    nb = 0
    assigned=0
    strokes = 1
    while freq:
        nb += sum(freq[:keys])*strokes
        strokes+=1
        freq=freq[keys:]
    print 'Case #%s: %s' % (i+1, nb)
