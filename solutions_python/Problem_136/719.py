import sys
path = ""
name = "B-small-attempt0"
sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")
tc = int(raw_input())
for cc in range(1, tc + 1):
	line = raw_input().split()
	c = float(line[0])
	f = float(line[1])
	x = float(line[2])
	time = 0.0
	have = 0.0
	speed = 2.0
	while(have<x):
		noSpeedUp = (x-have)/speed
		if(have > c):
			speedUp = (x-(have-c))/(speed+f)
		else:
			speedUp = x/(speed+f) + (c-have)/speed
		if(speedUp<noSpeedUp):
			if(have > c):
				have = have - c
			else:
				time = time + (c-have)/speed
				have = 0
			speed = speed + f
		else:
			time = time + (x-have)/speed
			have = x
	print 'Case #'+str(cc)+': '+str(time)
