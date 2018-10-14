import sys
line_number = 0

def algo(n, k):
	"""
	Return a tuple of two integers (in brackets below).
	o1o                 N=1 | K=[ 0,0 ]
	o1.o                N=2 | K=[ 1,0; 0,0 ]
	o.1.o               N=3 | K=[ 1,1; 0,0 x2 ]
	o.12.o              N=4 | K=[ 2,1; 1,0; 0,0 x2 ]

	o..1..o             N=5 | K=[ 2,2; 1,0 x2; 0,0 x2 ]
	o3.1.2.o            N=6 | K=[ 3,2; 1,1; 1,0; 0,0 x3 ]
	o.2.1.3.o           N=7 | K=[ 3,3; 1,1 x2; 0,0 x4 ]
	o.3.1.24.o          N=8 | K=[ 4,3; 2,1; 1,1; 1,0; 0,0 x4 ]

	o.24.1.35.o         N=9 | K=[ 4,4; 2,1 x2; 1,0 x2; 0,0 x4 ]
	o.34.15.26.o        N=10| K=[ 5,4; 2,2; 2,1; 1,0 x3; 0,0 x4 ]
	o4.25.1..3..o       N=11| K=[ 5,5; 2,2 x2; 1,0 x4; 0,0 x4 ]
	o..2.4.1..3.5.o     N=13| K=[ 6,6; 3,2 x2; 1,1 x2; 1,0 x2; 0,0 x6 ]
	o...2...1.......o   N=15| K=[ 7,7; 3,3 x2; 1,1 x4; 0,0 x8 ]
	o.6.2.48.1.7.3.59.o N=17| K=[ 8,8; 4,3 x2; 2,1 x2; 1,1 x2; 1,0 x2; 0,0 x8 ]
	"""
	if n == 1:
		return 0, 0
	elif n == 2:
		return (1 if k==1 else 0), 0

	if n % 2 == 1:
		if k == 1:
			return n//2, n//2
		else:
			return algo(n//2, k//2)
	else:
		if k == 1:
			return n//2, (n-1)//2
		else:
			if k % 2 == 1:
				return algo((n-1)//2, (k-1)//2)
			else:
				return algo(n//2, k//2)

for line in sys.stdin:
	if line_number:
		n, k = line.split()
		n = int(n); k = int(k)
		a, b = algo(n, k)
		print("Case #%d: %d %d" % (line_number, a, b))
	line_number += 1
