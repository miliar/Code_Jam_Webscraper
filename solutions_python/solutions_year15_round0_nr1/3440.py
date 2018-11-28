
T = input()
for i in range(T):
	maxs, s = raw_input().split()
	maxs = int(maxs)
	s1 = []
	for j in range(maxs+1):
		s1.append(int(s[j]))
	ans = 0
	sum = 0
	for k in range(len(s1)):
		for l in range(k):
			sum+=s1[l]
		if sum<k:
			ans+= k-sum
			s1[k]+= k-sum;
		sum = 0	
		
	print('Case #' + str(i+1) + ': ' + str(ans))
	
	
	
