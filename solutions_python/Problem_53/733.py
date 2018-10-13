def read_file(filename):
	testfile = open(filename)
	num = int(testfile.readline())
	for x in xrange(num):
		line = testfile.readline()
		n,k = map(int,line.split())
		if(k % 2**n == 2**n-1):
			print "Case #"+str(x+1)+": ON"
		else:
			print "Case #"+str(x+1)+": OFF"

read_file("A-large.in")
