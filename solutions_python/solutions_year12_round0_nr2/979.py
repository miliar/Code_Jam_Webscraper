def nosurpr(trs,p):
	return trs>=p+(p-1)*2
	
def wsurpr(trs,p):
	if (p<=2):
		return p<=trs
	else:
		return trs>=p+(p-2)*2

def solve():
	fi = open('gdance_large_in.txt','r')
	fo = open('gdance_large_out.txt','w')
	T = int(fi.readline())
	for t in xrange(1,T+1):
		inp = map(int,fi.readline().strip().split())
		n,s,p = inp[:3]
		sums = inp[3:]
		oksimple = 0
		oksurpr = 0
		for trs in sums:
			if nosurpr(trs,p):
				oksimple += 1
			elif wsurpr(trs,p):
				oksurpr += 1
#		print inp,n,s,p,sums,oksimple,oksurpr
		res = oksimple + min(s,oksurpr)
		fo.write("Case #%d: %d\n"%(t,res))
	fi.close()
	fo.close()
