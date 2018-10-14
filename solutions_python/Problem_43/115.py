from __future__ import with_statement
import copy
import sys

def count_unique(array):
    return len(dict(zip(array, range(len(array)))))

numerals = list("1023456789abcdefghijklmnopqrstuvwxyz")
def next_numeral(current):
    return numerals[numerals.index(current) + 1]

def min_base(string):
    unique = count_unique(string)
    translation = []
    
    rtt = {"1":string[0]}
    tt = {string[0]:"1"}
    curr = "1"
    for char in string:
        if char not in tt:
            curr = next_numeral(curr)
            tt[char] = curr
        translation.append(tt[char])
    tstring = "".join(translation)
    
    return int(tstring, max(unique, 2))

with open(sys.argv[1]) as f:
    lines = [l[:-1] for l in f.readlines()]
    for case,line in enumerate(lines[1:]):
        print "Case #%i: %i" % (case + 1, min_base(line))
    

