import sys

def main():

	data = sys.stdin.read().split("\n")
	T = int(data[0])
	data.pop(0)
	

	for i in xrange(0, T):
		print "Case #%s: %s" % (i+1, possible(data[0]))
		data.pop(0)

def possible(case):

	l = case.split(" ")
	N = int(l[0])
	Pd = int(l[1])
	Dg = int(l[2])

	Pworks = []	
	Dgworks = []

	for i in xrange(1, N+1):
		if (float(i*Pd)/float(100)) % 1 == 0 :

			if Pd < 100 and Dg == 100:
				return "Broken"
			elif Pd > 0 and Dg == 0:
				return "Broken"
			else: return "Possible"
	return "Broken"

main()
