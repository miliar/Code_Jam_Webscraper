test = input()
for t in range(0,test):
	s = raw_input()
	l = s.split()
	n = int(l[0])
	shy_list = list(l[1])
	shy_list = map(int,shy_list)
	count_stand = 0;
	friends = 0;
	for i in range(0,n+1):
		if count_stand >= i:
			count_stand += shy_list[i]
		else:
			friends += i-count_stand
			count_stand += i - count_stand + shy_list[i]
	print "Case #"+str(t+1)+": "+str(friends)