

T = input()

for c in range(1, T+1):
	N = [int(n) for n in str(input())]
	
	i = 0
	while i<len(N):
		j = 1
		while i+j<len(N) and N[i] == N[i+j]:
			j += 1
		if i+j == len(N):
			i += j
			break
		if N[i] > N[i+j]:
			break
		i += j
	if i<len(N)-1:
		N[i] -= 1
		for k in range(i+1, len(N)):
			N[k] = 9
	y = ""		
	for d in N:
		y += str(d)
	
	y = int(y)
	
	print "Case #"  + str(c) + ": " + str(y)