t=input()
for x in range(1,t+1):
	ans = input()
	for i in range(0,4):
		a=raw_input()
		if i==ans-1:
			b=a.split()

	ans = input()
	for i in range(0,4):
		a=raw_input()
		if i==ans-1:
			c=a.split()
	setb = set(b).intersection(c)
	cardn = len(setb) 
	if cardn == 0 :
		print "Case #"+str(x)+": "+"Volunteer cheated!"
	elif cardn == 1:
		print "Case #"+str(x)+": "+setb.pop()
	else :
		print "Case #"+str(x)+": "+"Bad magician!"
