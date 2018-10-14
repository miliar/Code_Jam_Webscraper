def main():
	t = int(input())
	
	for i in range(t):
		s = input().split()
		s, k = list(s[0]), int(s[1])
		l = len(s)
		c = 0
		
		for j in range(l-k+1):
			if s[j] == '-':
				s = rev(s, j, k)
				c += 1
			
		f = filter(lambda x: x == '-', s)	
		
		if len(list(f)) > 0:
			print("Case #", (i+1), ": IMPOSSIBLE", sep="")
		else:
			print("Case #", (i+1), ": ", c, sep="")
	
def rev(s, idx, k):
	r = {"+": "-", "-": "+"}
	
	for i in range(k):
		s[i+idx] = r[s[i+idx]]
		
	return s
	
main()