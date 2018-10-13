#!/usr/bin/python

import sys
from string import maketrans

fp = file(sys.argv[1])

#read params
n = int(fp.readline())

#read case
cases = (fp.readline() for x in range(n))

#read pattern
in_pattern  = "abcdefghijklmnopqrtsywvxzu"
out_pattern = "yhesocvxduiglbkrztwnafpmqj"
pattern = maketrans(in_pattern, out_pattern)

for i, word in enumerate(cases):
    word = word.translate(pattern)
    print "Case #{0}: {1}".format(i+1,word),

fp.close()

