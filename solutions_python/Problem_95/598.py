#!/usr/bin/env python

map = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q', 'q': 'z'}

#tran = 'our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up'

def translate(line):
    ar = []
    for w in line.split():
        tr = ''
        for i in range(len(w)):
            tr = tr + map[w[i]]
        ar.append(tr)
    return ' '.join(ar)

g = open('output', 'w')
with open("A-small-attempt0.in") as f:
    N = int(f.readline())
    for i in range(N):
        s = f.readline()
        out = 'Case #%d: %s\n' % (i+1, translate(s))
        g.write(out)
g.close()

#text = text.split()
#tran = tran.split()
#
#for k in range(len(text)):
#    for i in range(len(text[k])):
#        map[text[k][i]] = tran[k][i]
#
#print map
