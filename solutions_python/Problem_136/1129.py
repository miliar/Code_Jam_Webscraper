def solve_prob():
	[c,f,x] = [float(i) for i in input().split()]
	def get_cost(n):
		start_cost = 0
		for i in range(n):
			start_cost += c / (2 + i * f)
		return start_cost + x / (2 + n * f)
	def decreasing(n):
		return n==0 or get_cost(n-1) > get_cost(n)
	low,high = 0,int(x/c)+1
	while high - low > 1:
		mid = (low + high)//2
		if decreasing(mid):
			low = mid
		else:
			high = mid
	return get_cost(low)	
		

numcases = int(input())
for i in range(1,numcases+1):
	print("Case #%d: %f" % (i,solve_prob()))

