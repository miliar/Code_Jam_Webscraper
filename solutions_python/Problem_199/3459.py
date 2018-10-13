def flip(s,k,b):
	for i in range(k):
		if s[b+i]=='-':
			s[b+i]='+'
		else:
			s[b+i]='-'
def check(s):
	for i in range(len(s)):
		if s[i]=='-':
			return False
	return True

def sol(s,k):
	s = list(s)
	count=0
	i=0
	while i<=len(s)-k:
		if s[i]=='-':
			flip(s,k,i)
			count+=1
		i+=1
	if check(s):
		return count
	else:
		return -1



f = open("A-large.in")
wf = open("A-large-out.txt",'w')
data = []
for line in f:
	data.append(line)
cases = int(data[0])
for c in range(cases):
	p = data[c+1].split()
	s = p[0]
	k = int(p[1])
	count = sol(s,k)
	wf.write("Case #%s: "%(c+1))
	if (count==-1):
		wf.write("IMPOSSIBLE")
	else:
		wf.write(str(count))
	wf.write('\n')
