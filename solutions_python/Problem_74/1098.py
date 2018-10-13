#!/usr/bin/python

C=int(raw_input())

for case in range(C):
	row=raw_input().split()
	pushs=int(row[0])

	o=[]
	b=[]
	s=[]
	for push in range(pushs):
		robot=row[push*2+1]
		button=int(row[push*2+2])
		s.append([robot,button])
		if robot=='B':
			b.append(button)
		else:
			o.append(button)



	o.append(1)
	b.append(1)
	si=0
	bp=1
	bi=0
	op=1
	oi=0	

	time=0
	while si!=pushs:
		if s[si][0]=='O':
			if bp>b[bi]:
				bp-=1
			if bp<b[bi]:
				bp+=1					

			if s[si][1]==op:
				oi+=1
				if oi==len(o):
					oi-=1
				si+=1
			else:
				if op>o[oi]:
					op-=1
				if op<o[oi]:
					op+=1
		else:
			if op>o[oi]:
				op-=1
			if op<o[oi]:
				op+=1

			if s[si][1]==bp:
				bi+=1
				if bi==len(b):
					bi-=1
				si+=1
			else:
				if bp>b[bi]:
					bp-=1
				if bp<b[bi]:
					bp+=1					
		time+=1

	print "Case #"+str(case+1)+": "+str(time)	

