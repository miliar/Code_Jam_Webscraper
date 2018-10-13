
def headtail(l):
	return l[0], l[1:]

def sortstr(s):
	return "".join(sorted(s))

def res(line):
	
	# Nasty input parsing
	
	splt = line.split()
	
	c, r = int(splt[0]), splt[1:]
	combines_list, r = r[:c], r[c:]
	d, r = int(r[0]), r[1:]
	opposed_list, r = r[:d], r[d:]
	n, r = int(r[0]), r[1:]

	invokes = r[0]
	
	combines = dict( (sortstr(i[:2]), i[2]) for i in combines_list )
	
	opposed = map(sortstr, opposed_list)
	
	def combine(elist):
		while len(elist) > 1:
			rep = combines.get(sortstr(elist[-2:]))
			if rep is not None:
				elist[-2:] = [rep]
			else:
				break
				
	elist = []
	
	for i in invokes:
		
		# add
		elist += [i]
		
		# combine
		combine(elist)
		
		# remove if any elem is opposed to last one
		if any ( sortstr([elist[i], elist[-1]]) in opposed for i in xrange(len(elist)-1) ):
			elist = []

	return str(elist).replace("'", '')


if __name__ == "__main__":

	import sys

	filename = sys.argv[1]

	# Cut off case count
	caselines = open(filename).readlines()[1:]

	for case_no, line in enumerate(caselines, 1):

		print "Case #%d: %s" % (case_no, res(line))

