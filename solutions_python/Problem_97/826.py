import sys

# get command line arguments
if len(sys.argv) != 2:
        print 'Usage: '+sys.argv[0]+' input'
        sys.exit(-1)

# read input file
f = open(sys.argv[1],'r')
lines = f.readlines()
num_test_case = int(lines[0])

for i in range(num_test_case):
	count = 0
	used = []
	data = lines[i+1].split(' ')
	A = int(data[0])
	B = int(data[1])
	
	for j in range(A,B+1):
		curr = str(j)
		for k in range(len(curr)-1):
			next = curr[-1]+curr[:-1]
			x = int(next)
			if x <= B and x > j:
				pair = (j,x)
				if pair in used:
					continue
				count += 1
				used.append(pair)
				#print j,next,count
			curr = next
	#print i,count
	print 'Case #'+str(i+1)+': '+str(count)
		
