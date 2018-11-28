def is_recycle_numbers(a,b):
	if(len(a)!=len(b)):
		return False
	for i in range(len(a)-1):
		a=a[-1]+a[:-1]
		if(a==b):
			return True
	return False

import sys
readin=sys.stdin.readline
T=input()
for i in range(T):
	text=readin()
	text=text.split()
	A=int(text[0])
	B=int(text[1])
	count=0
	for n in range(A,B,1):
		for m in range(n+1,B+1,1):
			if is_recycle_numbers(str(n),str(m)):
				count+=1
	print 'Case #'+str(i+1)+': '+str(count)

	

