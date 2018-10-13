import sys

def search(s,k1):
	for x in range(k1,len(s)):
		if (s[x]==0):
			return x
	return -1


def fp(a,k1,l):
	for x in xrange(k1,k1+l):
		a[x]+=1
		a[x]%=2

def conv(s):
	a=[]
	for x in xrange(0,len(s)):
		if s[x] == '+':
			a.append(1)
		else:
			a.append(0)
	return a

T = raw_input().strip()
T = int(T)
k = []
S = []
for i in xrange(T):
	s = raw_input().strip().split(' ')
	S.append(s[0])
	k.append(int(s[1]))
	print S,T

z = []
flip = 0
for i in range(T):
	a=conv(S[i])
	f=search(a,0)
	m=0
	flag=0
	while(f!=-1):
		if(f>abs(len(S[i])-k[i])):
			flag=1
			break
		fp(a,f,k[i])
		f=search(a,f)		
		m+=1
	flag2=0
	if(flag):
		m=0
		while(f!=-1):
			if(f>abs(len(S[i])-k[i])):
				flag2=1
				break
			fp(a[::-1],f,k[i])
			f=search(a[::-1],f)
			m+=1
	if(flag2==0):
		z.append(m)
	else:
		z.append("IMPOSSIBLE")
	print z


output_filename=open('op.txt','w')
for i in range(T):
	#print 'Case #'+str(i+1)+': '+str(N[i])
	output_filename.write('Case #'+str(i+1)+': '+str(z[i]))
		
	output_filename.write('\n')
output_filename.close()

