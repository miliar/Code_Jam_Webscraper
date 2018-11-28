import sys
sys.stdin = open('stdin.txt','r')
sys.stdout = open('stdout.txt','w')
t=int(input())
for u in range(t):
	s=list(map(int,input().split()))
	n=s[0]
	r=s[1]
	y=s[3]
	b=s[5]
	f = True
	if(r>y+b):
		f=False
	elif(y>r+b):
		f=False
	elif(b>r+y):
		f=False
	if(f==False):
		print("Case #"+str(u+1)+": IMPOSSIBLE")
	else:
		s=""
		p=0
		i=0
		last = 'T'
		while(r>0 or y>0 or b>0):
			if(last=='R'):
				if(y>b):
					s+='Y'
					last = 'Y'
					y-=1
				else:
					s+='B'
					last = 'B'
					b-=1
			elif(last=='Y'):
				if(r>b):
					s+='R'
					last = 'R'
					r-=1
				else:
					s+='B'
					last = 'B'
					b-=1
			else:
				if(y>r):
					s+='Y'
					last = 'Y'
					y-=1
				else:
					s+='R'
					last = 'R'
					r-=1
		s=list(s)
		if(s[len(s)-1]==s[0]):
			temp = s[len(s)-1]
			s[len(s)-1] = s[len(s)-2]
			s[len(s)-2] = temp
		_s=""
		for i in s:
			_s+=i
		print("Case #"+str(u+1)+": "+_s)



