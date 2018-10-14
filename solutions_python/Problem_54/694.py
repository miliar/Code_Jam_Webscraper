#!/usr/bin/python

def gcd(no1,no2):
	if(no1 == 0):
		return no2
	elif(no2 == 0):
		return no1
	while no1!=no2:
		if no1>no2:
			no1-=no2
		elif no2>no1:
			no2-=no1  
	return no1

fp = open("B-small-attempt0.in", "r")
c = int(fp.readline())
for i in range(c):
	t = []
	line = fp.readline()
	line = line.strip()
	x = line.split()
	n = int(x[0])
	for j in range(n):
		t += [int(x[j+1])]
	if(n == 2):
		diff = abs(t[0] - t[1])
		closest = 0
		time = max(t[0], t[1])
		if(time%diff == 0):
			closest = time
		else:
			closest = int(int(time/diff) + 1)*diff
		time = closest - time;
	if(n == 3):
		diff3 = max(abs(t[0]-t[1]), abs(t[1]-t[2]), abs(t[2]-t[0]))
		diff3 = gcd(diff3, abs(t[0]-t[1]))
		diff3 = gcd(diff3, abs(t[1]-t[2]))
		diff3 = gcd(diff3, abs(t[2]-t[0]))
		time = max(t[0], t[1], t[2])
		if(time%diff3 == 0):
			closest = time
		else:
			closest = int(int(time/diff3) + 1)*diff3
		time = closest - time
	string = "Case #"+ str(i+1) +": "+str(time)
	print string
