def main():
	t = int(input())
	
	for i in range(t):
		print("Case #", (i+1), ": ", solve(), sep="")

def solve():
	n, k = input().split()
	n, k = int(n), int(k) - 1
	
	c = {n: 1}
	
	while k > 0:
		s = max(c.keys())
		n = min(c[s],k)
		k -= n
		
		a = int((s-1)/2)
		b = a + (s-1)%2 
		
		add(c,s,-n)
		add(c,a,n)
		add(c,b,n)
		check(c,s)
		
	s = max(c.keys())
	return ans(s)
		
def add(d, s, i):
	if s in d:
		d[s] += i
	else:
		d[s] = i
		
def check(d,s):
	if d[s] == 0:
		del d[s]

def ans(s):
	a = int((s-1)/2)
	b = a + (s-1)%2 
	
	return str(b)+" "+str(a)
	
main()