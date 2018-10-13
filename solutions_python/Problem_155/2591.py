def maxShy(shylist):
	maxdiff = 0
	runningsum = 0
	
	for i in range(len(shylist)-1):
		runningsum += int(shylist[i])
		maxdiff = max(maxdiff, i+1-runningsum)

	return maxdiff
		

f = open('in.in', 'r')
o = open('out.in', 'w')
T = int(f.readline())
for case in range(1, T+1):
	N = f.readline().split()

	maxshy = N[0]
	shylist = N[1]

	assert len(shylist)==int(maxshy)+1
	y = maxShy(shylist)
	o.write("Case #{0}: {1}\n".format(case, y))
	
