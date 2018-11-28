def gcd(a, b):
	if b > a:
		(a,b)=(b,a)
	if b == 0:
		return a
	else:
		return gcd(b, a-b*(a/b))

input = file('B-small-attempt0.in')
output = file('out','w')
numberofcases = int(input.readline())
for i in range(1, numberofcases+1):
	t = [int(x) for x in input.readline().split()][1:]
	t.sort()
	s = list(set(t))
	s.sort()
	for j in range(len(s)-1):
		s[j] = s[j+1]-s[j]
	s.pop()
	for j in range(len(s)-1):
		s[j+1] = gcd(s[j],s[j+1])
	t[0] = -t[0]
	while(t[0] < 0):
		t[0] = t[0]+s[-1]
	output.write("Case #"+str(i)+": "+str(t[0]))
	output.write("\n")
	
