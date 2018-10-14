import sys

filename = sys.argv[1]

fd = open(filename, 'r')
op = open('output.dat', 'w')
flag = 0
count = 0

for line in fd:
	if flag == 0:
		flag = 1
		continue
	elif flag == 1:
		flag = 2
		count += 1
		data = line.split()		
		r = int(data[0])
		k = int(data[1])
		n = int(data[2])
	elif flag == 2:
		groups = line.split()		
		groups = [int(x) for x in groups]
		earned = 0
		for i in range(r):
			tot = 0
			grps = n
			while((tot + groups[0] <= k) and grps > 0):
				grps -= 1
				tot += groups[0]	
				earned += groups[0]			
				temp = groups[0]
				groups.remove(groups[0])
				groups.append(temp)
		op.write("Case #" + str(count) + ": " + str(earned))
		op.write('\n')	
		flag = 1

		
	
	
		
