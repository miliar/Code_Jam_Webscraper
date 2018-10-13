lines = [line.strip() for line in open('A-large.in')]
A = []

total_testcases = lines[0].split()[0]
#print total_testcases
f = open("A-large.out", "w")
for num in range(1,int(total_testcases)+1):
	Smax = lines[num].split()[0]
	Str = lines[num].split()[1]
	#print Smax, Str
	#print Str[0]
	sum = 0
	min_invites = 0
	for k in range(int(Smax)+1):
		if ((k > sum) & (int(Str[k]) != 0)):
			min_invites = min_invites + (k-sum)
			sum = k
		sum = sum + int(Str[k])
	A.append('Case #{}: {}'.format(num, min_invites))
f.write("\n".join(A))
f.close()