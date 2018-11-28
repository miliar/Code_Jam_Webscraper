import sys
	
def prob(input):
	data = input.split()
	N = int(data[0])
	S = int(data[1])
	P = int(data[2])
	scores = data[3:]
	cases=0
#	print "N",N
#	print "S",S
#	print "P",P
#	print "scores",scores
	for s in scores:
		score = int(s)
		base = score/3
		result = ()
		if score % 3 == 0:
			if base >= P:
				cases = cases+1
			elif S>0 and base >0 and base+1>=P:
				cases = cases+1
				S=S-1
		elif score % 3 == 1:
			if base >= P or base+1 >= P:
				cases = cases+1
			elif S>0 and base+1 >=P:
				cases=cases+1
				S=S-1
		elif score % 3 == 2:
			if base+1>=P or  base >=P:
				cases=cases+1
			elif S>0 and base+2>=P:
				cases = cases+1
				S=S-1
	return cases
	
if __name__ == "__main__":
	f = sys.stdin
	if len(sys.argv) >= 2:
		fn = sys.argv[1]
		if fn != '-':
			f = open(fn)

	t = int(f.readline())
	for s in xrange(t):
		inp = f.readline()
		print "Case #%d: %d" %(s+1,prob(inp))