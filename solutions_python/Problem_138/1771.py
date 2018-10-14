fo = open("out","w")
tc=input()
for x in xrange(1,tc+1):
	war=0
	dwar=0
	l=input()
	n=map(float,raw_input().split())
	k=map(float,raw_input().split())
	n.sort()
	k.sort()
	nc=list(n)
	kc=list(k)
	while len(n)!=0:
		if n[-1]>k[-1]:
			war+=1
			k.pop(0)
		else:
			k.pop()
		n.pop()
	while len(nc)!=0:
		if nc[-1]>kc[-1]:
			dwar+=1
			nc.pop()
		else:
			nc.pop(0)
		kc.pop()
	fo.write("Case #"+`x`+": "+`dwar`+" "+`war`+"\n")
fo.close()