def calc(l,r):
	for i in range(1,len(l)):
		a, b = r/i, l[i]-l[i-1]
		n = a if a < b else b
		
		for j in range(i):
			l[j]+=n
			r-=n
			
		if a < b:
			break
			
	if r > 0:
		a, b = r/len(l), 1-l[0]
		n = a if a < b else b
		
		for i in range(len(l)):
			l[i]+=n	
			
	return l
	
def test():
	T, N = map(int, input().split())
	r = float(input())
	l = sorted(list(map(float, input().split())))
	a = calc(l,r)
	
	ans = 1
	for i in a:
		ans *= i
		
	return ans

def main():
	c = int(input())
	
	for i in range(c):
		print("Case #"+str(i+1)+": "+str(test()))
		
main()