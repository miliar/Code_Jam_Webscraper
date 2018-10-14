test = int(raw_input())
for x in range(test):
	s_max , inp = raw_input().split()
	inp = str(inp)
	counter = 0
	ans = 0
	temp = 0
	for j in range(len(inp)):
		if counter < j and inp[j] != '0':
			temp = abs(counter - j)
			counter += temp + int(inp[j])
			ans += temp
		else:
			counter += int(inp[j]) 
	print "Case #" + str(x+1) +": " + str(ans)  
