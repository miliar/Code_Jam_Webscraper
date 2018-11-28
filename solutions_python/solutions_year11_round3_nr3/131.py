def div(a,b):
	return int(1.0*a/b)==1.0*a/b

def solve():
	for i in range(L,H+1):
		ok=True
		for j in range(N):
			ff=freqs[j]
			if not (div(i,ff) or div(ff,i)):
				ok=False
				break 
		if ok:
			return i
	return "NO"

f=open("in.txt")
f_out=open("out.txt",'w')

Tests=int(f.readline().strip())
for case in range(1,Tests+1):
	N,L,H=map(int,f.readline().strip().split())
	#print R,C
	freqs=map(int,f.readline().strip().split())
	
	#print "inputs",N,L,H
	#print "freqs",freqs
	#print matrix
	ans=solve()
	
	f_out.write("Case #%d: %s\n" %(case,ans))
	#f_out.write("Case #%d:\n" %(case))
