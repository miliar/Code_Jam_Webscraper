def solve(N,PD,PG):
	if PG==0:
		if PD>0:
			return "Broken"
		else:
			return "Possible"
	if PG==100:
		if PD!=100:
			return "Broken"
		else:
			return "Possible"
	if N>=100:
		return "Possible"
	ok=False
	for D in range(N+1):
		if str(PD*D)[-2:]=="00":
			ok=True
			#print PD,D
		#print "N,PD,D,PD*D=WD",N,PD,D,PD*D
	
	if ok:
		return "Possible"
	return "Broken"

f=open("in.txt")
f_out=open("out.txt",'w')

Tests=int(f.readline().strip())
for case in range(1,Tests+1):
	N,PD,PG=map(int,f.readline().strip().split())
	ans=solve(N,PD,PG)
	f_out.write("Case #%d: %s\n" %(case,ans))
