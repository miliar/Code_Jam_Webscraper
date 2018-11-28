#! /usr/bin/env python

import sys, os

encoded = '''ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv'''

decoded = '''our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up'''

assert len(encoded) == len(decoded)

mapping = {}
for e,d in zip(encoded,decoded):
    if not mapping.has_key(e):
        mapping[e] = d
    else:
        assert mapping[e] == d

#finding missing chars
missing = []
for i in range(26):
    c = chr(97+i)
    if not mapping.has_key(c):
        missing.append(c)
print('missing keys %s' %  missing)
assert len(missing) == 2
mapping[missing[0]] = missing[1]
mapping[missing[1]] = missing[0]

print(mapping)

f = file(sys.argv[1])
lines = f.readlines()
f.close()

inputData = []
cases = int(lines[0].strip())

pos = 1
for c in range(cases):
    inputData.append( lines[pos].strip() )
    pos = pos + 1


def analyse(text):
    return ''.join( mapping[d] for d in text.strip())

output = []
for case,input in enumerate(inputData):
    print('case %i : inputs %s' % (case+1, input))
    res = analyse(input)
    output.append('Case #%i: %s' % (case+1, res))
    print(output[-1])

f = file(sys.argv[1].replace('.in','.out'),'w')
f.write('\n'.join(output))
f.close()
