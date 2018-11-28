#!/usr/bin/python

import sys

mapping = { 'a' : 'y', 'o' : 'e', 'z' : 'q', ' ' : ' ' }

allChars = [ chr(i) for i in range(97, 97+26) ] + [' ']

s = [ ("our language is impossible to understand",
       "ejp mysljylc kd kxveddknmc re jsicpdrysi"),
      ("there are twenty six factorial possibilities",
       "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"),
      ("so it is okay if you want to just give up",
       "de kr kd eoya kw aej tysr re ujdr lkgc jv")]

for x,y in s:
    for a,b in zip(x,y):
        mapping[a]=b

reverse = {}
missingIn = set(list(allChars))
missingOut = set(list(allChars))
for a,b in mapping.iteritems():
    reverse[b] = a
    missingIn.remove(a)
    missingOut.remove(b)

# assume single missing character
a = missingIn.pop()
b = missingOut.pop()
mapping[a] = b
reverse[b] = a

inputs = []
with open(sys.argv[1], 'r') as f_in:
    n = int(f_in.readline().strip())
    for l in f_in:
        inputs.append(l.strip())

translate = lambda c: reverse[c]

with open(sys.argv[1] + '.out', 'w') as f_out:
    for i, l in enumerate(inputs):
        f_out.write("Case #%i: " % (i+1))
        for c in l:
            f_out.write(reverse[c])
        #f_out.write(map(translate, l))
        f_out.write('\n')
