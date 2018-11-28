in_file = open("2.txt")
import sys
sys.setrecursionlimit(1000000)
best = 9999999.0
c = 0.0
f = 0.0
x = 0.0


t = int( in_file.readline().strip() )

def doit(time, rate):
	global c,f,x,best
	cur = float(time + (x / rate))
	if cur > best:
		return
	best = min(best , cur )

	doit( time + (c / rate) , rate + f)
'''
c = 500.0
f = 4.0
x = 2000.0
doit(0.0,2.0)
print best'''

for z in range(t):
	line = in_file.readline().strip().split()
	best = 9999999.0
	c = float(line[0])
	f = float(line[1])
	x = float(line[2])
	doit(0.0 , 2.0 )
	print "Case #{}: {:.7f}".format(z+1 , best)

'''
best = 9999999.0
c = 10.0
f = 1.0
x = 100000.0
doit(0.0 , 2.0 )
print "Case #{}: {:.7f}".format(z+1 , best)'''