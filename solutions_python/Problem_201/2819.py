import math as Math

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
	stalls, people = [int(s) for s in input().split(" ")]
	x=0
	y=0
	level = 0
	while people >= int(2 ** (level + 1)):
		level +=1
	stalls -= (2 ** level) - 1
	stallsLeft = stalls % (2 ** level)
	stalls /= 2 ** level
	stalls = Math.floor(stalls)
	if people - (2 ** level) <= stallsLeft - 1:
		stalls += 1
	x = Math.floor(stalls / 2)
	y = stalls -x - 1
	print('Case #%i: %i %i' % (i,x,y))  