def check(x,c,r,i):
	if x==1:
		print str("Case #")+str(i)+str(":")+str(" GABRIEL")
	elif x==2:
		sz=c*r
		if sz%2==0:
			print str("Case #")+str(i)+str(":")+str(" GABRIEL")
		else:
			print str("Case #")+str(i)+str(":")+str(" RICHARD")
	elif x==3:
		sz=c*r
		if (sz==6 or sz==12 or sz==9):
			print str("Case #")+str(i)+str(":")+str(" GABRIEL")
		else:
			print str("Case #")+str(i)+str(":")+str(" RICHARD")
	elif x==4:
		sz=c*r
		if(sz%4!=0):
			print str("Case #")+str(i)+str(":")+str(" RICHARD")	
		else:
			if(sz==12 or sz==16):
				print str("Case #")+str(i)+str(":")+str(" GABRIEL")
			else:
				print str("Case #")+str(i)+str(":")+str(" RICHARD")
	return

if __name__ == "__main__":
	t=input()
	for i in range(1,t+1):
		x,c,r=map(int,raw_input().split())
		check(x,c,r,i)
