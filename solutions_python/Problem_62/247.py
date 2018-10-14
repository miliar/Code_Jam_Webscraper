import sys
file = sys.argv[1]
input = open(file,'r')


def check(i,j):
	if (i[0] > j[0]):
		if (i[1] < j[1]): 
			return 1
		else:
			return 0
	else:
		if (i[1] > j[1]):
			return 1
		else:
			return 0
	
testcases = int(input.readline())
# there are t cases bt we will loop till end of file
for t in range (0, testcases):
	n_line = input.readline()
	n = int(n_line)
	result = 0
	wires = []
	# building list of all wires
	for i in range (n):
		line = input.readline()
		line = line.rstrip('\n')
		wire = list(line.split())
		wire[0] = int(wire[0])
		wire[1] = int(wire[1])
		wires.append(wire)
	
	#print  wires
	# loop to check every possible intersection
	for i in range (n):
		for j in range(n):
			if ( i != j ):
				if (check(wires[i],wires[j])):
					result = result + 1;
		
	# output	
	print "Case #"+str(t+1)+": "+ str(result/2)



