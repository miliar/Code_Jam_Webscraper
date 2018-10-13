#! /usr/bin/env python

import sys

first = lambda (x, y) : x
second = lambda (x, y) : y

class GError(Exception) :
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

def compute(surprise, best, scores) :
    total = best * 3
    if best > 0 : 
        cands = filter(lambda x: (x >= total-4) & (x != 0), scores)
    else : 
        return len(scores)
    supr = len(filter(lambda x : x < total - 2, cands))
    if supr <= surprise :  return len(cands)
    else : return (len(cands) - supr + surprise)
    
if len(sys.argv) <= 0 : sys.exit()

fname = sys.argv[1] 
fh = open (fname) 

case_count = int(fh.readline().strip())

for i in range(1, case_count+1) :
    nums = map(int, fh.readline().split())
    ss = nums[1]
    pp = nums[2]
    scores = nums[3:]
    print "Case #%d: %d" % (i, compute(ss, pp, scores))
    
fh.close()
