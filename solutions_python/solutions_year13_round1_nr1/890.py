#!/usr/bin/python3
import math

#каждый круг pi((t+1)^2-t^2)=pi(2t+1)
#2t+1, 2t+5, 2t+9
#s(n) = n(2r+1 + 2(n-1)) = 2rn+n+2nn-2n = 2nn-n+2rn
#найти такое n, при котором s(n) равно ma при заданном r
#ma = 2nn-n+2rn
#2nn+n(2r-1)-ma=0
def main():
	f = open('../test_files/input', 'r')
	w = open('../test_files/output', 'w')
	s = f.readline()
	t = int(s)
	for i in range(1, t+1):
		w.write("Case #%d: " % i)
		# r - первый радиус
		# ma - максимум краски
		r, ma = [int(x) for x in f.readline().split()]
		n = math.floor((1-2*r+math.sqrt(1+8*ma-4*r+4*r*r))/4)
		while n*(2*n-1+2*r) > ma:
			n -= 1
		w.write(str(n)+"\n")
	w.close()

if __name__ == '__main__':
	main()