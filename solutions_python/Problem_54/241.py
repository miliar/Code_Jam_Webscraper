def gcd(a,b):
	if a > b:
		c = a
		a = b
		b = c
	while a:
		a, b = b%a, a
	return b

fin = open("B-small.in", "r")
fout = open("B.out","w")
lines = fin.readlines();
T = int(lines[0])
for c in range(1,T+1):
	lol = lines[c].split()
	N = int(lol[0])
	nums = []
	for i in range(1,N+1):
		nums.append(int(lol[i]))
	difs = []
	for i in range(0,N-1):
		for j in range(1,N):
			difs.append(abs(nums[i]-nums[j]))
	di = difs[0]
	for i in range(1,len(difs)):
		di = gcd(di,difs[i])
	if nums[0]%di == 0:
		val = 0
	else:
		val = di - (nums[0]%di)
	s = 'Case #'+str(c)+': '+str(val)+'\n'
	fout.write(s)


	
		


		
