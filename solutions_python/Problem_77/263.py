#find the maximum object that is out of place
#find the last object that isnt sorted
#that takes two hits


f = open('goroinput.txt','r')
trials = int(f.readline())
def get_wrong_ones(right,wrong):
	bad = []
	for k in xrange(0,len(right)):
		if right[k] != wrong[k]:
			bad.append(right[k])
	return bad

for i in xrange(1,trials+1):
	num_elements = int(f.readline())
	elements = map(int,f.readline().split())
	sorted_elems = sorted(elements)
	#print elements
	#print sorted_elems
	wrong = get_wrong_ones(sorted_elems,elements)
	
	print "Case #%d: %f" % (i,len(wrong))