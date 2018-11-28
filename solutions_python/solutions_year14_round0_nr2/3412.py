import math
import sys

def main():
	fle = open(sys.argv[1],'r')
	times = int(fle.readline())
	for i in range(0,times):
		cf = fle.readline().split()
		c = float(cf[0])
		f = float(cf[1])
		x = float(cf[2])
		flag = True
		j = 1
		ans = 0
		prev = first(0,f,c,x)
		while (flag):
			next = first(j,f,c,x)
			if(next>prev):
				flag = False
				ans = prev
			prev = next
			j = j + 1
		print 'Case #'+str(i+1)+': '+ str("%.7f"%ans)
		
		

def first(n,f,c,x):
	time = 0
	rate = 2
	for pointer in range(0,n):
		x_time = c/rate
		rate = rate + f
		time = time + x_time
	x_time = x/rate
	time = time + x_time
	return time
main()
