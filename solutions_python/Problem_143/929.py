def parseint(s):
	s = s.split()
	return (int(s[0]), int(s[1]), int(s[2]))

def	process(filename):
	fin = open(filename,'r')
	tc = int(fin.readline())
	for t in range(0,tc):
		ans = 0
		(a,b,k) = parseint(fin.readline())
		for i in range(0,a):
			for ii in range(0,b):
				if i&ii < k:
					ans+=1
		print "Case #{0}: {1}".format(t+1, ans)
if __name__ == '__main__':
	import sys
	if len(sys.argv) != 2:
		sys.stderr.write("USAGE: %s <coll-file>\n" % sys.argv[0])
		ys.exit()	
	process(sys.argv[1])