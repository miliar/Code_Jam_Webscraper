t = int(input())

def istidy(n):
	e = [int(x) for x in list(str(n))]
	for i in range(1,len(e)):
		if e[i-1]>e[i]:
			return False
	return True

def tidy(n):
	for i in range(n,0,-1):
		if istidy(i):
			return i

def bigtidy(n):
	s = [int(x) for x in list(str(n))]
	l = len(s)
	i = 0
	while i < l-1:
		if i < 0:
			i = 0
		if s[i]>s[i+1]:
			s = s[:i] + [s[i]-1] + (l-i-1)*[9]
			i -= 2
			# return int("".join([str(c) for c in s]))
		i += 1
	return int("".join([str(c) for c in s]))


for i in range(t):
	n = int(input())
	r = bigtidy(n)
	print("Case #{}: {}".format(i+1, r))