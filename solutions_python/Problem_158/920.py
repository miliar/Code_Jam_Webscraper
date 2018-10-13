t=input()
for i in range(1,t+1):
	x,c,r=map(int,raw_input().split())
	temp=str("Case #")+str(i)+str(":")
	if x==1:
		print temp+str(" GABRIEL")
	elif x==2:
		sz=c*r
		if sz%2==0:
			print temp+str(" GABRIEL")
		else:
			print temp+str(" RICHARD")
	elif x==3:
		sz=c*r
		if (sz==6 or sz==12 or sz==9):
			print temp+str(" GABRIEL")
		else:
			print temp+str(" RICHARD")
	elif x==4:
		sz=c*r
		if(sz%4!=0):
			print temp+str(" RICHARD")	
		else:
			if(sz==12 or sz==16):
				print temp+str(" GABRIEL")
			else:
				print temp+str(" RICHARD")
