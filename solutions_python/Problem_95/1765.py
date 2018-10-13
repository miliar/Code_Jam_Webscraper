#!/usr/bin/env python3
# vim:set ts=8 sw=4 et smarttab:
# Qualification Round 2012

import sys
import string

sample_input = '''ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv'''
sample_output = '''our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up'''

assert len(sample_input) == len(sample_output)

mapping = dict()
mapping['y'] = 'a'
mapping['e'] = 'o'
mapping['q'] = 'z'

mapping_range = set()
mapping_range.add('a')
mapping_range.add('o')
mapping_range.add('z')

for i in range(len(sample_input)):
    if sample_input[i].isalpha():
        if sample_input[i] in mapping:
            assert mapping[sample_input[i]] == sample_output[i]
        else:
            mapping[sample_input[i]] = sample_output[i]
            assert sample_output[i] not in mapping_range
            mapping_range.add(sample_output[i])

not_in_domain = [ch for ch in string.ascii_lowercase if ch not in mapping]
not_in_range = [ch for ch in string.ascii_lowercase if ch not in mapping_range]

assert len(not_in_domain) == len(not_in_range)
assert len(not_in_domain) <= 1
assert len(not_in_range) <= 1

if len(not_in_domain) == 1:
    mapping[not_in_domain[0]] = not_in_range[0]

line = sys.stdin.readline()
fields = line.split()
assert len(fields) == 1
ntc = int(fields[0])

for tc in range(1, ntc + 1):
    line = sys.stdin.readline()
    line = list(line)
    if line[-1] == '\n':
        del line[-1]
    for i in range(len(line)):
        if line[i].isalpha():
            line[i] = mapping[line[i]]
    line = ''.join(line)
    print('Case #{0}: {1}'.format(tc, line))
