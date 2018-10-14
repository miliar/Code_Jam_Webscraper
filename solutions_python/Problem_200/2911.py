def tidy(s):
	if len(s) > 1:	
		for i in range(0,len(s)-1):
			if s[i]>s[i+1]:
				return False
	return True

def solve():
	r=open('read.txt','r')
	f=open('out.txt','w')
	#t=int(input())
	t = int(r.readline())	
	for i in range(1,t+1):
		#ans=input()
		ans = str(r.readline())[:-1]
		n = int(ans)	
		temp=1
		if not tidy(ans):
			while temp<=len(ans):		
				ans = str(n-n%10**(temp)-1)	
				n = int(ans)
				if tidy(ans):
					break
				temp = temp+1
		#print('Case #'+str(i)+': '+ans)
		f.write('Case #'+str(i)+': '+ans+'\n')
	r.close()	
	f.close()
solve()
