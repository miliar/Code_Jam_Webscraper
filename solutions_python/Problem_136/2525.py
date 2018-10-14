import sys

fi = open(sys.argv[1],'r')
t = int(fi.readline())


for caseno in range(t):
	input = []
	tot_time = 0.0
	r = 2.0
	fin = fi.readline()
	input = [float(x) for x in fin.split()] 
	c = input[0]
	f = input[1]
	x = input[2]
	while True:
		t1 = tot_time + (x/r)
		t2 = tot_time + (c/r) + (x/(r+f))
		if t1 < t2 :
			break
		else : 
			tot_time = tot_time + (c/r)
			r = r + f
	print "Case #"+str(caseno+1)+":",
	print "%.7f" % t1
