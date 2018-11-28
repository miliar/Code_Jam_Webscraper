import sys

f=sys.stdin
fout=sys.stdout
case_num=int(f.readline())
#print case_num
for i in range(case_num):
	info=f.readline()
	#print info
	use=info.split()
	X=int(use[0])
	R=int(use[1])
	C=int(use[2])
	#print X, R,C
	if X==1:
		print "Case #"+str(i+1)+": "+"GABRIEL"
	elif X==2:
		if (R*C)%2==0:
			print "Case #"+str(i+1)+": "+"GABRIEL"
		else:
			print "Case #"+str(i+1)+": "+"RICHARD" 
	elif X==3:
		if (R*C)%3==0 and (R*C)>3:
			print "Case #"+str(i+1)+": "+"GABRIEL"
		else:
			print "Case #"+str(i+1)+": "+"RICHARD" 
	elif X==4:
		if (R*C)%4==0 and (R*C>8):
			print "Case #"+str(i+1)+": "+"GABRIEL"
		else:
			print "Case #"+str(i+1)+": "+"RICHARD" 

sys.stdout=fout
fout.close()