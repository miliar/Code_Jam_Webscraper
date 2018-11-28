import math
t= input()
t1=0
while t1<t:
	t1=t1+1
	line1= raw_input()
	D=int(line1.split(" ")[0])
	N= int(line1.split(" ")[1])
	n1=0
	max1=float(0.00)
	while n1 <N:
		hors1 = raw_input().split(" ")
		k1=float(hors1[0])
		s1= float(hors1[1])
		diff= float(D)-k1
		time1= float(diff)/s1
		#print time1
		if (max1 <time1):
			max1=time1
		n1=n1+1
	if max1==0:
		op_speed=float(0)
	else:
		op_speed=float(D/max1)
	#op_speed1 = round(op_speed, 6)
	#print '%.6f' % op_speed
	print "Case #%d: %.6f"%(t1,op_speed)
		