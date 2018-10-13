T = int(input())

def is_inc(r):
	s = str(r)
	for i in range(1,len(s)):
		if int(s[i-1]) > int(s[i]):
			return False
	return True

for t in range(0,T):
	N = int(input())
	#print("N = {}".format(N))
	while not is_inc(N):
		N -= 1
	print("Case #{}: {}".format(t+1,N))
