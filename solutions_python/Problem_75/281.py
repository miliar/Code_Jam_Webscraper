from itertools import *

infile = "B-large.in"

lines = [s.rstrip() for s in open(infile, "rb").readlines()]
NCases=int(lines[0])

for i,caseline in enumerate(lines[1:]):
	items = caseline.split(" ")
	
	ncombine = int(items[0])
	combines = items[1:1+ncombine]
	items = items[1+ncombine:]
	
	ndestroy = int(items[0])
	destroy = items[1:1+ndestroy]
	items = items[1+ndestroy:]
	
	nchars = int(items[0])
	spellstr = items[1:][0]
	
	combine_table = {}
	for comb in combines:
		c1, c2, cnew = comb[0], comb[1], comb[2]
		combine_table[(c1, c2)] = cnew
		combine_table[(c2, c1)] = cnew
	destroy_table = set()
	for des in destroy:
		c1, c2 = des[0], des[1]
		destroy_table.add((c1, c2))
		destroy_table.add((c2, c1))
	
	result = []
	#print spellstr
	for c in spellstr:
		#print "result:",result, c
		if (len(result) >= 1 and ((result[-1], c) in combine_table)):
			newc = combine_table[(result[-1], c)]
			result.pop()
			result.append(newc)
		elif ( any([((c, ci) in destroy_table) for ci in result] )):
		#c in result and ((result[-1], c) in destroy_table)):
			result = []
		else:
			result.append(c)

	print "Case #%d: [%s]" %(i+1, ", ".join(result))
	