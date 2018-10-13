output=open("Output.txt","w")
t=input()
for testcases in range(t):
	n=input()
	if(not n%10):
		n-=1
	s=str(n)
	if(len(s)>1 and s[0]=='1' and '0' in s):
		print "Hello"
		res=""
		for i in range(1,len(s)):
			res+='9'
		n=int(res)
	elif("10" in s):
		print "Hello2"
		temp=0
		for i in range(len(s)):
			if(s[i]=='1'):
				temp=i-1
				break
		res=s[:temp]
		res+=str(int(s[temp])-1)
		for i in range(temp+1,len(s)):
			res+='9'
		n=int(res)
	elif('0' in s):
		print "Hello3"
		temp=0
		for i in range(len(s)-1):
			if(s[i+1]=='0'):
				res=s[:i]
				res+=str(int(s[i])-1)
				temp=i+1
				break
		for i in range(temp,len(s)):
			res+='9'
		n=int(res)
	s=str(n)
	temp=0
	loop2=False
	c='a'
	for i in range(len(s)-1):
		if(int(s[i])>int(s[i+1])):
			res=s[:i+1]
			res+=str(int(s[i+1])-1)
			temp=i+2
			loop2=True
			c=s[i]
			break
	if(loop2):
		found=True
		res=""
		for i in range(len(s)):
			if(s[i]==c and found):
				res+=str(int(s[i])-1)
				found=False
			elif(found):
				res+=s[i]
			else:
				res+='9'
		n=int(res)
	print n
	print "Case #"+str(testcases+1)+": "+str(n)
	output.write("Case #"+str(testcases+1)+": "+str(n)+"\n")
