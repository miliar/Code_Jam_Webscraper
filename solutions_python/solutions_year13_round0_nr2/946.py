import sys

def solve(lawn):
	out=[]
	for r in lawn:
		mh = max(r)
		out.append([mh for i in range(len(r))])
	#print lawn, out
	for c in range(len(lawn[0])):
		cl = [r[c] for r in lawn]
		mh = max(cl)
		for j in range(len(cl)):
			if out[j][c]>mh:
				out[j][c] = mh 
	#print lawn, out	
	for r in range(len(lawn)):
		if lawn[r] != out[r]:
			return 'NO'
	return 'YES'
			




N = int(sys.stdin.readline().strip())

for t in range (N):
	M = int(sys.stdin.readline().strip().split(" ")[0])
	lawn = []
	for r in range(M):
		lawn.append([int(h) for h in sys.stdin.readline().strip().split(" ")])
	
	print "Case #{0}: {1}".format(t+1, solve(lawn))