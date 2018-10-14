import math

input = open('input2.in', 'r')
output = open('output2.out', 'w');

cases = int(input.readline())

i = 0
while i < cases:
	r = 2
	line = input.readline()
	line = line.rstrip().split(' ')

	c = float(line[0])
	print c    
	f = float(line[1])
	print f
	x = float(line[2])
	print x
	sum = 0.0

	if (x<=c):
		time = x/r
	else:
			time = 0
			while sum < x:
				time = time + c/r
				print c/r
				sum = sum + c
				t1 = (x - sum)/r
				t2 = (x - sum + c)/(r+f)
				if t1>t2:
					sum = sum - c
					r = r +f
					print time
				else:
					print time
					time = time + ((x-sum)/r)
					print r
					print time
					sum = x

	print 'Do'

	output.write("Case #"+str(i+1)+": "+str(time)+"\n")

	i = i + 1

output.close()
