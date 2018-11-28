#!/usr/bin/env python

import sys

letters = 'abcdefghijklmnopqrstuvwxyz '

g_sample = ['q',
'ejp mysljylc kd kxveddknmc re jsicpdrysi',
'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
'de kr kd eoya kw aej tysr re ujdr lkgc jv']

e_sample = ['z',
'our language is impossible to understand',
'there are twenty six factorial possibilities',
'so it is okay if you want to just give up']

rosetta = {}
for g_l, e_l in zip(g_sample, e_sample):
    for g_c, e_c in zip(g_l, e_l):
        print g_c, e_c
        if g_c not in rosetta:
            rosetta[g_c] = e_c
        elif rosetta[g_c] != e_c:
            print 'ERROR: %s is mapped to %s not %s' % (g_c, rosetta[g_c], e_c)

#print len(rosetta)        
#print rosetta

#mapped = rosetta.values()
#unmapped = [l for l in letters if l not in mapped]

#for letter in letters:
#    if letter not in rosetta.keys():
#        print 'no match for: %s' % letter
#        print 'could be one of: %s' % ''.join(unmapped)
rosetta['z'] = 'q'

g_file = open(sys.argv[1])
g_file.next()

outfile = open('googlerese.out.txt','w')
case = 1
for line in g_file:
    outfile.write('Case #%i: ' % case)
    case += 1
    for c in line.strip():
        outfile.write(rosetta[c])
    outfile.write('\n')
