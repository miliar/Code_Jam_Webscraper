t=int(raw_input())
for i1 in range (1,t+1):
	n=int(raw_input())
	temp=raw_input()
	Na = [float(i) for i in temp.split()]
	temp=raw_input()
	Ke = [float(i) for i in temp.split()]
	Na1=list(Ke)
	Ke1=list(Na)
	winN=0
	winK=0
	t1=0
	t2=0
	while Na:
		try:
			blah=min(Na)
			asasd=min(x for x in Ke if x > blah)
			#print "number =",blah
			#print  "min=", asasd
			Na.remove(blah)
			Ke.remove(asasd)
			winK=winK+1
			#print Na
			#print Ke
		except ValueError:
			#print "number =",blah
			#print  "blah=", asasd
			
			Ke.remove(min(Ke))
			Na.remove(blah)
			winN=winN+1
			#print Na
			#print Ke



	while Na1:
		try:
			blah=min(Na1)
			asasd=min(x for x in Ke1 if x > blah)
			#print "number =",blah
			#print  "min=", asasd
			Na1.remove(blah)
			Ke1.remove(asasd)
			t1=t1+1
		except ValueError:
			Ke1.remove(min(Ke1))
			Na1.remove(blah)
			t2=t2+1
		

	#print t1, winN
	print "Case #%i: %d %d" %(i1,t1,winN)

