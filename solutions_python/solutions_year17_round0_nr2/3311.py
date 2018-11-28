def ok(x):
	for i in range(1,len(s)):
		if x[i]>=x[i-1]:
			continue
		else:
			return False
	return True

def gao(s):
	for i in range(len(s)-1-1,-1,-1):
		if s[i]=='0':
			continue
		temp = s[:i]+str(int(s[i])-1)+'9'*(len(s)-1-i-1+1)
		if ok(temp) and int(temp)<=int(s):
			return temp


n=int(input())
for cs in range(n):
	s=input()
	org = int(s)

	if ok(s):
		print("Case #{0}: {1}".format(cs+1,s))
		continue

	s=gao(s)

	
	print("Case #{0}: {1}".format(cs+1,int(s)))

