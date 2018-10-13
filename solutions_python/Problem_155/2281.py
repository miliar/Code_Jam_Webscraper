with open("input","r") as inp, open("output","w") as out:
	num_tc = int(inp.readline())
	for i in range(num_tc):
		tc = inp.readline().split()
		sum = int(tc[1][0])
		ans = 0
		for j in range(len(tc[1])-1):
			if int(tc[1][j+1])!=0 and j+1>sum:
				ans+= j+1 - sum
				sum+= j+1 - sum
			sum+=int(tc[1][j+1])
		out.write("Case #" + str(i+1) + ": " + str(ans) + "\n")