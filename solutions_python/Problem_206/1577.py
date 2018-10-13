import math

d = 0
n = 0
startd = 0
s = 0
time = 0
remaind = 0
largesttime = 0
maxspeed = 0

t = int(input())

for i in range(1,t+1):

	d = 0
	n = 0
	startd = 0
	s = 0
	time = 0
	remaind = 0
	largesttime = 0
	maxspeed = 0
	a = 0
	b = 0

	d,n = [int(x) for x in input().split(" ")]

	for q in range(1,n+1):
		startd,s = [int(x) for x in input().split(" ")]
		remaind = d-startd
		time = remaind/s

		if time > largesttime:
			largesttime = time

	maxspeed = d/largesttime
	a = len(str(int(maxspeed)))
	b = a+1+6
	maxspeed = "{0:.8f}".format(maxspeed)
	maxspeed = str(maxspeed)
	maxspeed = maxspeed[0:b]

	print ("Case #{}: {}".format(i,maxspeed))