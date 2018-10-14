def flip(s,k,j):
	s = list(s)
	for i in range(k):
		if s[j+i] == "-":
			s[j+i] = "+"
		else:
			s[j+i] = "-"
	return "".join(s)

def rec(tried,n,k,d):
	nn = {}
	if not n:
		return 0, 0
	for s in n:
		if s.count('-') == 0:
			return 1, d
		tried[s] = 0
		for i in range(len(s)+1-k):
			ss = flip(s,k,i)
			if ss not in tried:
				nn[ss] = 0
	return rec(tried,nn,k,d+1)
	

t = int(input())
for i in range(1, t + 1):
	s = input().split(" ")
	k = (int(s[1]))
	s = s[0]
	tried = {}
	n = {s:0}
	ok, r = rec(tried,n,k,0)
	if ok:
		print("Case #{}: {}".format(i, r))
	else:
		print("Case #{}: IMPOSSIBLE".format(i,))
