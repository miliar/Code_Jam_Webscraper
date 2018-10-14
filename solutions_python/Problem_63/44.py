from math import *

if __name__=='__main__':
	a = raw_input();
	T = eval(a);


	for qqq in range(T):
		a = raw_input()
		a=a.split()
		L = eval(a[0])
		P = eval(a[1])
		C = eval(a[2])

		times = ceil(P/float(L))

		counter = 0

		while times > C:
			times = ceil(sqrt(times))
			counter+=1

		print 'Case #%d: %d'% (qqq+1, counter)
