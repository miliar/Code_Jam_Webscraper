import sys
sys.stdin = open ('B-large.in')
sys.stdout = open ('B.txt','w')

T = int(input().strip())

for z in range (T):
	c,f,x = map(float,input().strip().split())
	rate = 2.0
	time = x/rate
	while time > time-((x-c)/rate)+(x/(rate+f)):
		time-=(x-c)/rate
		rate+=f
		time+=x/rate
	print ('Case #{0}:'.format(z+1),'%0.7f' % (time))

sys.stdout.close()