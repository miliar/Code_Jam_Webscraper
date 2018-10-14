import sys, math

count = sys.stdin.readline();

def shift(n, shiftn):
	digits = int(math.floor(math.log10(n))+1)
	
	shifted = n * int(math.pow(10,shiftn))
	
	head = shifted % int(math.pow(10,digits))
	tail = int(math.floor(shifted / int(math.pow(10,digits))))
	shifted = head + tail
	
	return shifted


case = 0;
for line in sys.stdin:
	case += 1
	ints = line.split()
	a = int(ints[0])
	b = int(ints[1])
	
	total = 0
	
	shifts = int(math.floor(math.log10(a)))
	
	for n in xrange(a, b):
		recycled = []
		for shiftn in xrange(1, shifts+1):
			shifted = shift(n,shiftn)
			if (shifted > n) and (shifted <= b) and (shifted <> n):
				if (n not in recycled):
					recycled.append(n)
				if (shifted not in recycled):
					recycled.append(shifted)
					#print "(" + str(n) +", "+str(shifted)+ ")"
					total = total+1 # count distinct pairs
					
	print "Case #" + str(case) + ": " + str(total)
