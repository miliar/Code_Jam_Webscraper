import sys
readin=sys.stdin.readline
T=input()
for i in range(T):
	text=readin()
	text=text[:-1]
	text=text.split()
	for j in range(len(text)):
		text[j]=int(text[j])
	N=text.pop(0)
	S=text.pop(0)
	P=text.pop(0)
	c=0
	for j in range(N):
		if(text[j]<P):
			continue
		if text[j]>=3*P-2:
			c+=1
		elif S>0 and text[j]>=3*P-4:
			c+=1
			S-=1
	print 'Case #' + str(i+1) + ': '+str(c)
