#-*-coding:utf-8-*-

import os, sys, re

example = """ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up""".split('\n')

mapper = {}
mapped = set()
for i in range(3):
    text_in = example[i]
    text_out = example[i + 3]
    for j in range(len(text_in)):
        mapped.add(text_out[j])
        mapper[text_in[j]] = text_out[j]
        pass
    pass
rest_in = []
rest_out = []
for c in 'abcdefghijklmnopqrstuvwxyz ':
    if c not in mapped: rest_out.append(c)
    if c not in mapper: rest_in.append(c)
    pass

mapper['z'] = 'q'
mapper['q'] = 'z'

fh =open(sys.argv[1])
for i in range(int(fh.readline())):
    text_in = fh.readline().strip()
    sys.stdout.write('Case #{0}: '.format(i + 1))
    for c in text_in:
        sys.stdout.write(mapper[c])
        pass
    sys.stdout.write('\n')
