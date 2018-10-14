T=input()
for i in range(1,T+1):
	line=raw_input().strip().split()
	C=float(line[0])
	F=float(line[1])
	X=float(line[2])
	time=1
	next_time=-1
	farms=0
	total_time=0
	while next_time  < time:
		time=(X/((farms*F)+2))+total_time
		next_time=(C/((farms*F)+2)) + (X/(((farms+1)*F)+2)) +total_time
		total_time+=C/((farms*F)+2)
		farms+=1
	print "Case #%i: %.7f"%(i,time)
	
