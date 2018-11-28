def flip(s,j,k):
	for i in range(j,j+k):
		if s[i] == '-':
			s[i] = '+'
		else:
			s[i] = '-'
	return s 

t = int(input().strip())
for i in range(1,t+1):
	s, k = input().strip().split()
	k = int(k)
	s = list(s)
	flips = 0
	for j in range(len(s)-k+1):
		if s[j] == '-':
			s = flip(s,j,k)
			flips += 1

	if '-' in s:
		print ("Case #{}: {}".format(i, "IMPOSSIBLE"))
	else:
		print ("Case #{}: {}".format(i, flips))