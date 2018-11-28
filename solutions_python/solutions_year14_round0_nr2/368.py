t = int(input())
for testcase in range(1, t+1):
	c, f, x = map(float, input().split())
	p = 2.0
	t = 0
	while (f*x>f*c+p*c):
		t+=c/p
		p+=f
	t+=x/p
	print("Case #" + str(testcase) + ": " + str(t))
