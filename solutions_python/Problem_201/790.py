def exe3(n,m):
	batch=1
	free_seats=n
	output=[]
	while(m>0):
		if m<=batch:
			temp = free_seats%batch
			if temp>0 and temp>=m: #lost div
				free_seats=free_seats/batch
			else:
				free_seats=free_seats/batch-1
			if free_seats%2==1:	
				output.append(free_seats/2+1)
			output.append(free_seats/2)
			return output
		else:
			m=m-batch
			free_seats -=batch
			batch *=2


t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
	n, m = [str(s) for s in raw_input().split(" ")]
	output = exe3(int(n),int(m))
	print "Case #{}: {} {}".format(i,max(output),min(output))
