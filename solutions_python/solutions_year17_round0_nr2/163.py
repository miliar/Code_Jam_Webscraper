def solve(m):
	n=len(m)
	inc_pre=0
	for i in range(1,n):
		if m[i-1] <= m[i]:
			inc_pre = i
		else:
			break
	if inc_pre == n-1:
		return m
	while(inc_pre > 0 and m[inc_pre] == m[inc_pre-1]):
		inc_pre -= 1
	res = m[:inc_pre] + dec(m[inc_pre])+('9'*(n-inc_pre-1))
	return res

def dec(x):
	return str(int(x)-1)

T = int(input())
for case in range(1,T+1):
	n=input()
	print("Case #{}: {}".format(case, str(int(solve(n)))))
