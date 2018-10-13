input = file('A-large.in')
output = file('out', 'w')
numOfCase = int(input.readline())
for i in range(1,numOfCase+1):
	n= [int(x) for x in input.readline().split()]
	if (n[1]+1) % (2**n[0]) == 0:
		output.write("Case #"+str(i)+": ON")
	else:
		output.write("Case #"+str(i)+": OFF")
	output.write("\n")
