#!/usr/bin/env python3

import sys

examples = [
    ('y qee',
     'a zoo',
    ),
    ('ejp mysljylc kd kxveddknmc re jsicpdrysi',
     'our language is impossible to understand'
    ),
    ('rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
     'there are twenty six factorial possibilities'
    ),
    ('de kr kd eoya kw aej tysr re ujdr lkgc jv',
     'so it is okay if you want to just give up'
    ),
    ('z',
     'q'
    ),
]

mapping = {}
resolved = set()


for google, normal in examples:
    for g, n in zip(google, normal):
        if g in mapping:
            assert mapping[g] == n, "Inconsistent mapping for %r" % g
        else:
            mapping[g] = n
            resolved.add(n)

for codepoint in range(ord('a'), ord('z') + 1):
    char = chr(codepoint)
    if char not in mapping:
        print('cannot map from', char)
    if char not in resolved:
        print('cannot map to', char)


# 3
# ejp mysljylc kd kxveddknmc re jsicpdrysi
# rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
# de kr kd eoya kw aej tysr re ujdr lkgc jv
# 
# Output
# Case #1: our language is impossible to understand
# Case #2: there are twenty six factorial possibilities
# Case #3: so it is okay if you want to just give up


def unscramble(string):
    return ''.join(mapping[c] for c in string)


for i, line in enumerate(sys.stdin):
    if i == 0:
        continue
    print("Case #%d: %s" % (i, unscramble(line.strip())))
