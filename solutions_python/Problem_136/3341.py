import math
import sys
fx=open(sys.argv[1],'r')
case = int(fx.readline())
def timex(n,f,c,x):
	time = 0
	rate = 2
	capital = 0
	case = 0
	while(case != n):
		time = time + 1
		capital = capital + rate
		if(capital >= c):
			capital = capital - c
			rate = rate + f
			case = case + 1
	towin = x - capital
	print 'n:'+str(n)
	print 'time:'+str(time+(towin/rate))
def m(n,f,c,x):
	time = 0
	rate = 2
	for pointer in range(0,n):
		expected_time = c/rate
		rate = rate + f
		time = time + expected_time
	expected_time = x/rate
	time = time + expected_time
	return time
		

for mpointer in range(0,case):
	cfx = fx.readline().split()
	c = float(cfx[0])
	f = float(cfx[1])
	x = float(cfx[2])
	is_Running = True
	pointer = 1
	ans = 0
	prev = m(0,f,c,x)
	while (is_Running):
		nextx = m(pointer,f,c,x)
		if(nextx>prev):
			is_Running = False
			ans = prev
		prev = nextx
		pointer = pointer + 1
	print 'Case #'+str(mpointer+1)+': '+ str("%.7f"%ans)
		
