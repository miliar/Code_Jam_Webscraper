import sys
t=sys.stdin.readlines()
k=len(t)
f=0
s=''
w=0
print "Case #1:"
for i in range(0,k):
	p=t[i]
	q=0
	while(q<len(p)):
		w=0
		if(t[i][q] == '/'):
			#print "Case #2:"
			if(q<(len(p)-1)):
				#print "Case #3:"
				if(t[i][q+1] == '*'):
					#print "Case #4:"
					f=f+1
					q=q+1
					w=1
		elif(t[i][q]=='*'):
			if(q<(len(p)-1)):
				if(t[i][q+1] == '/'and f>0):
					f=f-1
					q=q+1
					w=1
		if(f==0 and w==0 and t[i][q]!= '\n'):
			s=s+t[i][q]
		q=q+1
	if(f==0):
		print s
		s=''
		

		
		

