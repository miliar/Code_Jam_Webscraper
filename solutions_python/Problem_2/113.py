import sys

readline = sys.stdin.readline
def readstrlist():
	return readline().split()

def ttomin(t):
	h,m = map(int,t.split(':'))
	return h*60+m

def count (tA, tB, turn):
	#print '-', turn
	need = 0
	n = 0
	t = -turn
	for train in tA:
		was=train[0]-turn
		n += len (list(tb for tb in tB if tb[1]>t and tb[1]<=was))
		#print train, t,was,n, need
		if n == 0:
			need += 1
		else:
			n -= 1
		t = was
	return need

if __name__ == "__main__":
	for i in range(1, int(readline())+1):
		turn = int(readline())
		na,nb = map(int,readstrlist())
		
		tA=[]
		for j in range(na):
			tA.append (map(ttomin, readstrlist()))
		tA.sort()
		tB=[]
		for j in range(nb):
			tB.append (map(ttomin, readstrlist()))
		tB.sort()
		
		#print tA, tB
		
		
		print "Case #%d: %d %d" % (i, count(tA, tB, turn), count(tB, tA, turn))