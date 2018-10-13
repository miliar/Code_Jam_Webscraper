def f(n,li):
	n = int(n)
	s = 0
	ans = 0
	for i in range(n+1):
		if(i > s and i-s > ans):
			ans = i-s
		s += int(li[i])
	return ans

for i in range(int(input())):
	print("Case #{}: {}".format(i+1,f(*input().strip().split())))
