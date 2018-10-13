#!/usr/bin/python

#@ucefkh 2014 fb.com/ucefkh
#~ Problem B. Cookie Clicker Alpha 
#~ 2014/04/12 00:19:36

def cookies(c,f,x):
	rate,won,sec = 2,0,float(0)
	while won < x: #every second win f
		
		if won == 0:
			t1 = float(x)/(rate+f)+ float(c) /rate 
			t2 = float(x)/rate
			if t1 > t2:
				sec += t2
				won += x
			else: #buy farm :)
				sec += float(c) /rate 
				rate += f
		else:
			sec+=float(1)

	return sec		



df = file("B-large.in")

cases = int(df.readline())
n=cases
c,f,x = 0.0,0.0,0.0 #lol not special effects :D	

while cases :
	print "Case #{0}:".format(n-cases+1),
	c,f,x = map(float,df.readline().strip().split(' '))
	#~ print cookies(map(float,df.readline().strip().split(' ')))
	print "%.7f" % cookies(c,f,x)
	cases-=1
