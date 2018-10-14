from __future__ import division

a=raw_input()
cases=[]
for i in range(int(a)):
	values=raw_input()
	vv=values.split()
	row=[float(v) for v in vv]
	cases.append(row)

for j in range(len(cases)):
	ct=cases[j]
	C=ct[0]
	F=ct[1]
	X=ct[2]
	f=2
	t=1
	a=X/f
	b=X/(f+t*F)+t*C/f
	while a>b:
		t+=1
		a=b
		b=X/(f+t*F)
		eps=0
		for i in range(t):
			eps+=C/(f+F*i)
		b+=eps
	print 'Case #%i: %f' %(j+1,a)
