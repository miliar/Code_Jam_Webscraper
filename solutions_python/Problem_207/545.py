import sys
from math import ceil

T = int(sys.stdin.readline())

for k in xrange(T):
	N,R,O,Y,G,B,V = map(int, sys.stdin.readline()[:-1].split(" "))
	

	if N % 2 == 0:
		if R > N/2 or B > N/2 or Y > N/2:
			print "Case #{}: {}".format(k+1, "IMPOSSIBLE")
			continue
	else:
		if R >= ceil(N/2.0) or B >= ceil(N/2.0) or Y >= ceil(N/2.0):
			print "Case #{}: {}".format(k+1, "IMPOSSIBLE")
			continue

	ans = []
	Rs = "R" * R
	Bs = "B" * B
	Ys = "Y" * Y

	if R >= Y and R >= B:
		biggest = "R"
		Ys = "0" * (R-Y) + Ys
		Bs = Bs + "0" * (R-B)
		ans = map("".join,zip(Rs,Bs,Ys))
	elif B >= Y and B >= R:
		biggest = "B"
		Ys = "0" * (B-Y) + Ys
		Rs = Rs + "0" * (B-R)
		ans = map("".join,zip(Bs,Rs,Ys))
	elif Y >= R and Y >= B:
		biggest = "Y"
		Rs = "0" * (Y-R) + Rs
		Bs = Bs + "0" * (Y-B)
		ans = map("".join,zip(Ys,Bs,Rs))

	#ans = map("".join,zip(Rs,Bs,Ys))

	ans = "".join(ans)
	ans = ans.replace("0","")
	print "Case #{}: {}".format(k+1, ans)