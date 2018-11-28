def nondec(n):
	s = str(n)
	for i in range(len(s)-1):
		if s[i+1]<s[i]:
			return False
	return True

def sol(n):
	i = long(n)
	while i!=0:
		if nondec(i):
			return i
		i-=1


f = open("B-small-attempt0.in")
wf = open("B-out.txt",'w')
data = []
for line in f:
	data.append(line)
cases = int(data[0])
for c in range(cases):
	n = data[c+1]
	res = sol(n)
	wf.write("Case #%s: "%(c+1))
	wf.write(str(res))
	wf.write('\n')