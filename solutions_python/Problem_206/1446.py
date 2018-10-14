import sys

N = int(sys.stdin.readline())
#print N


i =0
while(i< N):
	i=i+1
	elems = sys.stdin.readline().split()
	D = int(elems[0])
	H = int(elems[1])
	#print("%s %s" % (D,H))
	j =0
	time = list()
	slowest = 0
	while(j<H):
		j=j+1
		elems2 = sys.stdin.readline().split()
		DJ = D-int(elems2[0])
		HJ = int(elems2[1])
		#print("%s %s" % (DJ,HJ))
		hiz = float(DJ)/HJ
		if hiz > slowest:
			slowest = hiz
		
	print  "Case #%d: %f" % (i, D/slowest)
		

