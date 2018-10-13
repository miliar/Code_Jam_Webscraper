dict1 = {' ': ' ',
 'a': 'y',
 'b': 'n',
 'c': 'f',
 'd': 'i',
 'e': 'c',
 'f': 'w',
 'g': 'l',
 'h': 'b',
 'i': 'k',
 'j': 'u',
 'k': 'o',
 'l': 'm',
 'm': 'x',
 'n': 's',
 'o': 'e',
 'p': 'v',
 'q': 'z',
 'r': 'p',
 's': 'd',
 't': 'r',
 'u': 'j',
 'v': 'g',
 'w': 't',
 'x': 'h',
 'y': 'a',
 'z': 'q'}

dict = {}
for k, v in dict1.iteritems():
    dict[v] = k

import sys
import os

file = sys.argv[1]
out = open(os.path.basename(file) + '.out', 'w')
with open(file, 'r') as f:
    for i, line in enumerate(f):
        if not i:
            continue
        line = line.strip()
        out.write('Case #%d: %s\n' % (i, ''.join([dict[c] for c in line])))
