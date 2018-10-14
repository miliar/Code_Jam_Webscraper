import sys, string
import itertools

def readlist():
	return [int(x) for x in sys.stdin.readline().strip().split(" ")]

P = int(sys.stdin.readline())

for p in range(P):
	L = sys.stdin.readline().strip().split(" ")[1:]
	
	to,tb = 0,0
	po,pb = 1,1
	rp = L[0]
	first=1
	for r,k in zip(L[0::2],L[1::2]):
		#~ print r,k
		k = int(k)

		if r == 'O':
			to += abs(k-po)
			po = k
		else:
			tb += abs(k-pb)
			pb = k

		if rp != r:
			#~ if first:
				#~ first = 0
			#~ else:
				if r == 'O':
					to = max(to,tb)
				else:
					tb = max(to,tb)
				

		if r == 'O':
			to += 1
			po = k
		else:
			tb += 1
			pb = k
		rp = r
		#~ print to,po,tb,pb

	ans = max(to,tb)
	print "Case #%d: %d" % (p+1, ans)
