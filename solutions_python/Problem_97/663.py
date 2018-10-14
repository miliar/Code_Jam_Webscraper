import sys


def get_m(s, i):
	return int( s[i+1:] + s[0:i+1] )

def solve(a, b):
	count = 0
	mapper = {}
	for n in range(a,b):
		s = str(n)
		for i in range(0, len(s)-1):
			if ( '0' != s[i+1] ):
				m = get_m(s, i)
				if ( m > n  and \
					m <= b and \
					(s+"_"+str(m)) not in mapper):
					count = count + 1
					mapper[s + "_" + str(m)] = 1
	return count

infile = open(sys.argv[1]).read().splitlines()[1:]

for i in range(0, len(infile)):
	a,b = [int(j) for j in infile[i].split(" ")]
	print "Case #" + str(i+1) + ": " + str(solve(a,b))
