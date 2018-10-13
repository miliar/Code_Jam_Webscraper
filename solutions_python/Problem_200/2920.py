
def tidy(N):
	s=list(N)
	n=int(N)
	if len(s)==1:
		return(N)
	else:
		b=True
		c='kg'
		for i in range(len(s)-1):
			#print (int(s[-i]))
			#print (int(s[-i-1]))
			if int(s[i])>int(s[i+1]):
				s[i]=str(int(s[i])-1)
				c='monk'
				break
		for j in range(i+1,len(s)):
				s[j]='9'	
		if c=='kg':
			return(N)
		else:
			N=''.join(s)
			n=int(N)
			N=str(n)
			return(tidy(N))

f=open(r'C:\Users\PRANAV CHAKRA VARTHY\Desktop\B-large.in') # reads the file
g=open(r'C:\Users\PRANAV CHAKRA VARTHY\Desktop\cj2-large.out','w')
f.readline()
count=1
for i in f: #reads every line (may be)
	k=i.strip('\n')
	ans=tidy(k) # computes the function
	g.write('Case #'+str(count)+': '+ans)
	g.write('\n')
	count+=1

g.close()
f.close()