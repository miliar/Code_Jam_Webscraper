def doit(x):
	s = str(n)
	i = 0
	prev = s[i]
	i+=1
	no = ''
	no+=s[0]
	while(i<len(s) and s[i]>=prev):
		no+=s[i]
		prev = s[i]
		i+=1
	if(i==len(s)):
		return n
	ans = int(no)-1
	if(ans == 0):
		ans = ''
	ans = str(ans)
	while(i<len(s)):
		ans+='9'
		i+=1
	return ans

def check(x):
	x = str(x)
	i = 1
	while(i<len(x)):
		if(x[i]<x[i-1]):
			return 0
		i+=1
	return 1


t = int(input())
test = 1
while test<=t:
	n = int(input())
	while(check(n)!=1):
		n = int(n)
		n = doit(n)
	answer = 'Case #'
	answer+=str(test)
	answer+=str(': ')
	answer+=str(n)
	
	print answer
	test+=1