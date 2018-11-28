def isTidy(n):
	s = list(str(n))
	for i in range(0,len(s)-1):
		if (s[i] <= s[i+1]) == False:
			return i
	
	return n
	
def solve(n):
	tidyChk = False
	while(tidyChk == False):
		tidy = isTidy(n)
		if len(str(n)) == 1:
			return n
		if tidy == n:
			return n
		else:
			s = list(str(n))
			s[tidy] = str(int(s[tidy])-1)
			for i in range(tidy+1, len(s)):
				s[i] = str(9)
			n = int("".join(s))
	
t=int(input())
for cas in range(1,t+1):
	n = int(input())
	print ("Case #{}: {}".format(cas,solve(n)))

	