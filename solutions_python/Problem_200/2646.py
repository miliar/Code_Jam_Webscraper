sol=''
for test in range(int(input())):
	S=input()
	s=[ x for x in S]
	l=len(s)
	ans=[]
	minus=False

	def makeall():
		for X in range(len(ans)):
			ans[X]='9'
	for i in range(l-1,0,-1):
		if minus:
			if s[i]=='0':
				makeall()
				ans.append('9')
			else:
				minus=False
				s[i]=chr(ord(s[i])-1)
				if s[i]<s[i-1]:
					ans.append('9')
					makeall()
					minus=True
				else:
					ans+=s[i]
		else:
			if s[i]=='0':
				makeall()
				ans.append('9')
				minus=True
			elif s[i]<s[i-1]:
				ans.append('9')
				makeall()
				minus=True
			else:
				ans.append(s[i])
		#print(i,ans,s)
	if minus:
		if s[0]!='1':
			ans.append(chr(ord(s[0])-1))
	else:
		ans.append(s[0])
	#print(0,ans,s)
	#print(ans[::-1])
	sol+='Case #'+str(test+1)+": "+''.join(ans[::-1])+'\n'
print(sol[:-1])