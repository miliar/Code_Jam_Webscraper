# Google Code Jam 2008
# Cheers, philzilla

import re
import sys
import math

class CodeJammer:
    regexp_cache = {}
    def __init__(self, inputfile):                          self.input_file = open(inputfile); self.output_file = open(inputfile[:inputfile.rfind(".")]+".out.txt", "w")
    def read_int(self):                                     return int(self.input_file.readline())
    def read_ints(self, ntimes):                            return [int(self.input_file.readline()) for x in xrange(ntimes)]
    def read_string(self):                                  return self.input_file.readline()
    def read_strings(self, ntimes):                         return [self.input_file.readline() for x in xrange(ntimes)]
    def read_pattern(self, pattern, func=None):
        mapping = {"I":("(\\d+)",int), "F":("(\\d+\.\\d+)",float), "S":("(\\S+)",str), " ":("(\\s+)",None)}
        groups = self.read_pattern_raw("".join([mapping.get(l,(re.escape(l),None))[0] for l in pattern]))
        r = tuple([cf(val) for cf,val in zip([mapping[l][1] for l in pattern if mapping.has_key(l)], list(groups)) if cf])
        if func: return func(r)
        else: return r
    def read_patterns(self, pattern, ntimes, func=None):    return [self.read_pattern(pattern, func) for x in xrange(ntimes)]
    def read_pattern_raw(self, pattern):
        if self.regexp_cache.has_key(pattern): regexp = self.regexp_cache[pattern]
        else: regexp = re.compile(pattern); self.regexp_cache[pattern] = regexp
        return regexp.match(self.input_file.readline()).groups()[:]
    def read_patterns_raw(self, pattern, ntimes):           return [self.read_pattern_raw(pattern) for x in xrange(ntimes)]
    def run(self, case_func):
        for i in range(self.read_int()):
            resultstr = "Case #%d: %s" % (i+1," ".join([str(x) for x in case_func(self)]))
            print >> self.output_file, resultstr; print resultstr

def testcase(cj):
	n = cj.read_int()
	la = [int(x) for x in cj.read_string().split()]
	lb = [int(x) for x in cj.read_string().split()]
	lbp = []
	lb.sort()
	la.sort()
	lb.reverse()
	return [sum([x*y for x,y in zip(la, lb)])]

p = CodeJammer("A-large.in")
p.run(testcase)
	