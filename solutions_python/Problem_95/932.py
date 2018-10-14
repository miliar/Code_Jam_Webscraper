#!/usr/bin/env python

f = open("a.in", "r")

data = f.readlines()

#print data
#print int(data[0])

fout = open("a.out", "w")

for i in range (1, int(data[0])+1):
    l = data[i].rstrip('\n')
#    print l
    s = list(l)
    for j in range(0,len(l)):
        if s[j] == 'a': s[j] = 'y'
        elif s[j] == 'b': s[j] = 'h'
        elif s[j] == 'c': s[j] = 'e'
        elif s[j] == 'd': s[j] = 's'
        elif s[j] == 'e': s[j] = 'o'
        elif s[j] == 'f': s[j] = 'c'
        elif s[j] == 'g': s[j] = 'v'
        elif s[j] == 'h': s[j] = 'x'
        elif s[j] == 'i': s[j] = 'd'
        elif s[j] == 'j': s[j] = 'u'
        elif s[j] == 'k': s[j] = 'i'
        elif s[j] == 'l': s[j] = 'g'
        elif s[j] == 'm': s[j] = 'l'
        elif s[j] == 'n': s[j] = 'b'
        elif s[j] == 'o': s[j] = 'k'
        elif s[j] == 'p': s[j] = 'r'
        elif s[j] == 'q': s[j] = 'z'
        elif s[j] == 'r': s[j] = 't'
        elif s[j] == 's': s[j] = 'n'
        elif s[j] == 't': s[j] = 'w'
        elif s[j] == 'u': s[j] = 'j'
        elif s[j] == 'v': s[j] = 'p'
        elif s[j] == 'w': s[j] = 'f'
        elif s[j] == 'x': s[j] = 'm'
        elif s[j] == 'y': s[j] = 'a'
        elif s[j] == 'z': s[j] = 'q'
        
    l = "".join(s)
    res = "Case #{0}: {1}\n".format(i, l)
    print res
    fout.write(res)

