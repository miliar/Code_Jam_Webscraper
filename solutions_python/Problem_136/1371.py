
def solve(Case):
	(C, F, X) = map(float, raw_input().split(' '))
	ans = []
	rate = 2.0
	ans.append(X/2.0)
	i = 1
	pre_cost = 0
	while (True):
		pre_cost += C/rate
		rate = rate + F
		rem_time = X/rate
		ans.append(rem_time+pre_cost)
		if ans[i-1] < ans[i]:
			break
		i += 1
	print 'Case #%d: %.7f'%(Case, ans[i-1])

def main():
	t = int(raw_input())
	for i in range(0, t):
		solve(i+1)

main()