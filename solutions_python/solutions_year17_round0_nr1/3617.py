from UserString import MutableString
f=open("pancake.txt","w")
t=input()
def flip(s):
	if(s=='+'):
		return '-'
	return '+'
for testcase in range(1,t+1):
	s,k=raw_input().split()
	s=MutableString(s)
	k=int(k)
	count=0
	for i in range(len(s)-(k-1)):
		if(s[i]=='-'):
			for j in range(i,i+k):
				s[j]=flip(s[j])
			count+=1
	is_happy=True
	for i in range(len(s)):
		if(s[i]=='-'):
			is_happy=False
			break
	if(is_happy):
		f.write("Case #"+str(testcase)+": "+str(count)+"\n")
	else:
		f.write("Case #"+str(testcase)+": "+"IMPOSSIBLE\n")
