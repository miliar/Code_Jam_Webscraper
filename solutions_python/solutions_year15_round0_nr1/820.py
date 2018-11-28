T = input()


for tc in range(T):
	M, row = raw_input().split()
	
	count = 0
	needed = 0
	for i in range(int(M)+1):
		if i > count and int(row[i]) > 0:
			needed += i - count;
			count += i - count;
		
		count += int(row[i])
		
	print "Case #" + str(int(tc) + 1) + ": " + str(needed)


