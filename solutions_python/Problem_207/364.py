import sys

sys.stdin = open('B-small-attempt1.in')
sys.stdout = open('B-small-attempt1.out', 'w')
 
N=0
R=0
O=0
Y=0
G=0
B=0
V=0
RR=0
YY=0
BB=0
rs = ""

def solve():
	global N
	global R
	global O
	global Y
	global G
	global B
	global V
	global RR
	global YY
	global BB
	global rs

	R = 0
	N, R, O, Y, G, B, V = map(int, sys.stdin.readline().strip().split())

	mx = max(R,Y,B)
	rs = ""

	RR=0
	YY=0
	BB=0

	def INCR():
		global N
		global R
		global O
		global Y
		global G
		global B
		global V
		global RR
		global YY
		global BB
		global rs
		R-=1
		RR+=1
		rs += "R"

	def INCY():
		global N
		global R
		global O
		global Y
		global G
		global B
		global V
		global RR
		global YY
		global BB
		global rs
		Y-=1
		YY+=1
		rs += "Y"

	def INCB():
		global N
		global R
		global O
		global Y
		global G
		global B
		global V
		global RR
		global YY
		global BB
		global rs
		B-=1
		BB+=1
		rs += "B"



	if (R is mx):
		INCR()
	elif (Y is mx):
		INCY()
	elif (B is mx):
		INCB()

	def rory():
		global N
		global R
		global O
		global Y
		global G
		global B
		global V
		global RR
		global YY
		global BB
		global rs
		if R>Y:
			INCR()
		elif R<Y:
			INCY()
		elif rs[0] is 'R':
			INCR()
		else:
			INCY()

	def yorb():
		global N
		global R
		global O
		global Y
		global G
		global B
		global V
		global RR
		global YY
		global BB
		global rs
		if Y>B:
			INCY()
		elif Y<B:
			INCB()
		elif rs[0] is 'Y':
			INCY()
		else:
			INCB()

	def rorb():
		global N
		global R
		global O
		global Y
		global G
		global B
		global V
		global RR
		global YY
		global BB
		global rs
		if R>B:
			INCR()
		elif R<B:
			INCB()
		elif rs[0] is 'R':
			INCR()
		else:
			INCB() 
		
	

	mx = max(R,Y,B)
	while (mx is not 0):
		if (rs[-1] is 'R'):
			yorb()
		elif(rs[-1] is 'Y'):
			rorb()
		elif(rs[-1] is 'B'):
			rory()
		
		if min(R,Y,B) < 0:
			return "IMPOSSIBLE"

		mx = max(R,Y,B)


	if (rs[0]==rs[-1]):
		return "IMPOSSIBLE"
	else:
		return rs

T = int(sys.stdin.readline())
for x in xrange(T):
	print("Case #" + str(x+1) + ": " + solve())