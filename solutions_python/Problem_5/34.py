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
	nmilk = cj.read_int()
	ncust = cj.read_int()
	likeset = set()
	clikes = []
	for c in range(ncust):
		likes = [int(x) for x in cj.read_string().split()]
		clikes.append([(likes[2*i+1]-1, likes[2*i+2]) for i in range(len(likes)/2)])
	for clike in clikes:
		for lt in clike:
			if lt[0] == 1:
				likeset.add(lt[0]+nmilk)
			else:
				likeset.add(lt[0])
	minv = nmilk + 1
	mint = []
	for i in range(2**nmilk):
		t = [[0,1][((i / 2**j) % 2 == 1)] for j in range(nmilk)]
		allhappy = True
		for clike in clikes:
			happy = False
			for lt in clike:
				if lt[1] == 1 and t[lt[0]] == 1:
					happy = True
					break
				if lt[1] == 0 and t[lt[0]] == 0:
					happy = True
			if not happy:
				allhappy = False
				break
		if allhappy:
			if sum(t) < minv:
				minv = sum(t)
				mint = t
			print "all happy with", sum(t), t
	if minv <= nmilk:
		return mint
	else:
		return ["IMPOSSIBLE"]

p = CodeJammer("B-small-attempt1.in")
p.run(testcase)
	