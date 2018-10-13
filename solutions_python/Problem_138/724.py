T=input()
for tt in range(T) :
	N=input()
	naomi=sorted(map(float,raw_input().split()))
	ken=sorted(map(float,raw_input().split()))

	naomi.reverse()
	ken.reverse()

	y=0
	for k in ken :
		if naomi[y]>k :
			y+=1

	z=0
	i=0
	for n in naomi :
		if ken[i]>n :
			i+=1
		else :
			z+=1

	print "Case #%d:"%(tt+1),y,z

		




