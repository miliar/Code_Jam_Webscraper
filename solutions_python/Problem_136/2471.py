case=0
f=open('B-large.in','r')
f1=open('output.in','w')
for inp in f:
	break;
input=int(inp)
for x in range(input):
	a=f.readline()
	i=0
	for m in a.split():
		if(i==0):
			C=float(m);
		elif(i==1):
			F=float(m)
		else:
			X=float(m)
		i+=1
	time=0.0
	rate=2
	cookie=0.0
	if(X<=C):
		time=X/rate
		case+=1
		f1.write("Case #"+str(case)+": "+str(time)+"\n")
		print("Case #"+str(case)+": "+str(time))
	else:
		while True:
			time_a=0.0#time for completion without farm
			time_b=0.0#time for completion with farm
			time_c=0.0#time for farm
			time_d=0.0#time for completion directly
			time_a=(X-C)/rate
			time_b=X/(rate+F)
			time_c=C/rate
			time_d=X/rate
			if((time_c+min(time_b,time_a))<time_d):
				time+=time_c
				if(time_a<time_b):
					time+=time_a
					case+=1
					f1.write("case #"+str(case)+": "+str(time)+"\n")
					print("case #"+str(case)+": "+str(time))
					break
				else:
					rate+=F
			else:
				time+=time_d
				case+=1
				f1.write("case #"+str(case)+": "+str(time)+"\n")
				print("case #"+str(case)+": "+str(time))
				break
			#print("TIME : "+str(time))