def check(s):
	length=len(s)
	for i in xrange(1,length):
		if int(s[i])<int(s[i-1]):
			return False
	return True
def tidy(s):
	length,flag=len(s),True
	nines,ans='',''
	for i in xrange(length):
		nines+='9'
	for i in xrange(1,length):
		if int(s[i])<int(s[i-1]):
			ans=s[:i-1]+str(int(s[i-1])-1)+'9'+nines[i+1:]
			flag=False
			break
	if flag:
		return int(s)
	return int(ans) if check(ans) else int(tidy(ans))
for t in xrange(1,input()+1):
	n=input()
	print 'Case',('#'+str(t)+':'),tidy(str(n))