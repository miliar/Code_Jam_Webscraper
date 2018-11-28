t=input()
for x in range(1,t+1):
	a = raw_input();
	speed=2
	C,F,X=[float(y) for y in a.strip().split()];
	time = 0
	while True :
		if (X-C)/speed > X/(speed+F):
			time = time + C/speed
			speed = speed + F
		else :
			time = time + X/speed
			break;
	print "Case #"+str(x)+": "+'%.7f'%time
	
