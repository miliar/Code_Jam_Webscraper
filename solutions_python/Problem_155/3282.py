import sys

T=int(raw_input())
case=1
while case<T+1:
	l=raw_input().split()

	inv=0
	aud=0
	s=int(l[0])
	for i,k in enumerate(l[1]):
		#print "Shyness:%d, Audience:%d"%(i,aud)
		add=0
		if i>aud:
			#print "Added %d"%(i-aud)
			add=i-aud
			inv+=add
		aud+=int(k)+add

	print "Case #"+str(case)+": "+str(inv)
	case+=1
