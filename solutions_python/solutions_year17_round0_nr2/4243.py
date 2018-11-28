T = input()
for i in range(T):
	flag = 0
	ans = ''
	temp = input()
	N = list(str(temp))
	while(flag != -1):
		flag = -1
		for j in range(len(N)-1):
			if (N[j]>N[j+1]):
				temp = int(N[j]) - 1
				N[j] = str(temp)
				flag = j
				break;
		if (flag != -1):
			for j in range(len(N)-flag-1):
				N[flag+j+1] = str(9)
	for k in N:
		ans= ans+k
	temp = int(ans)
	print ("Case #"+str(i+1)+": "+str(temp))