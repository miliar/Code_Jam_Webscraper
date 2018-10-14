import sys

def parse(s):
	x = []
	i = 0
	a = s[i]
	count = 0

	while i < len(s):
		if s[i] == a:
			count += 1
		else:
			x.append( (a,count) )
			count = 1
			a = s[i]
		i += 1
	x.append( (a,count) )
	return x		

f = open(sys.argv[1])
f.readline()
casenum = 1

n = f.readline()
while n != "":
	n = int(n)
	strings = [f.readline().strip() for i in xrange(n)]

	s1 = parse(strings[0])
	s2 = parse(strings[1])

	output = 0

	if len(s1) != len(s2):
		output = -1
	else:
		for x,y in zip(s1,s2):
			if x[0] != y[0]:
				output = -1
				break
			else:	
				output += abs(y[1]-x[1])

	#print strings
	#print s1, s2

	if output == -1:
		output = "Fegla Won"
	
	print "Case #{}: {}".format(casenum,output)
	n = f.readline()
	casenum += 1