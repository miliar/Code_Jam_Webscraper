inputfile = open('B-small-attempt0.in.txt')
outputfile = open('result.txt','w')

c=0
f=0
x=0

no_of_tests = int(inputfile.readline())

for t in range(no_of_tests):
	values = inputfile.readline().split()
	c = float(values[0])
	f = float(values[1])
	x = float(values[2])
	t1=0
	t2=0
	total_time=0
	no_farms=0

	while t2 <= t1:
		r1 = no_farms*f+2.0
		t1 = total_time+x/r1
		r2 = (no_farms+1)*f+2.0
		t2 = total_time+c/r1+x/r2
		no_farms+=1
		total_time += c/r1

	
		
			
		
	print >>outputfile,"Case #%d: %.7f" % (t+1,t1)
	


