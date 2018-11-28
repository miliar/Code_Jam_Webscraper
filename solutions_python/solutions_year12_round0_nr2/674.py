import sys

def get_min_max(val):	
	if ( 0 == val ):
		return [0, 0]
	elif ( 0 == val % 3):
		return [val/3, val/3+1]
	elif ( 1 == val % 3):
		return [val/3+1, val/3+1]
	else:
		return [val/3+1, val/3+2]

def solve(n, s, p, a):
	count = 0

	for i in range(0, len(a)):
		min, max = get_min_max(a[i])
		if ( min >= p):
			count = count + ( len(a) - i )
			break
		elif ( s > 0 and max >=p ):
			count = count + 1
			s = s - 1
	
	return count
infile = open(sys.argv[1]).read().splitlines()[1:]

for i in range(0, len(infile)):
	a = [int(j) for j in infile[i].split(" ")]
	[n,s,p] = a[0:3]
	a = sorted(a[3:])
	print "Case #" + str(i+1) + ": " + str(solve(n,s,p,a))
