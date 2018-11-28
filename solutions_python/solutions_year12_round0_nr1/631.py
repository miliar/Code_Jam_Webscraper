#!/usr/bin/env python

def create_mapping_from_data():
    mapping = {}
    cipher = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
    clear = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"
    for index, cipher_char in enumerate(cipher):
        mapping[cipher_char] = clear[index]
    return mapping

import sys

test_file = open(sys.argv[1])

mapping = create_mapping_from_data()

# from the problem description
mapping['y'] = 'a'
mapping['e'] = 'o'
mapping['q'] = 'z'

# missing from the problem description data
mapping['z'] = 'q'

num_lines = int(test_file.readline())
for numline in xrange(num_lines):
    line = test_file.readline().strip()
    out_list = [mapping[c] for c in line]
    print "Case #%d: %s"%(numline+1, ''.join(out_list))

