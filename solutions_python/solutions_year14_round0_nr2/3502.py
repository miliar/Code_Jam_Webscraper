from decimal import *
getcontext().prec = 28
fin = open('b.in', 'r')
out = open('b.out', 'w')
a = fin.readline()
for cases in range(int(a)):
	[c,f,x]=fin.readline().split(" ")
	[c,f,x]=[Decimal(c),Decimal(f),Decimal(x)]
	time=Decimal(0)
	rate=Decimal(2)
	while 1:
		fin1 = (x/rate+time).quantize(Decimal('.0000001'), rounding=ROUND_HALF_DOWN)
		fin2 = (x/(rate+f)+time+c/rate).quantize(Decimal('.000001'), rounding=ROUND_HALF_DOWN)
		if fin2 < fin1:
			time = time + c/rate
			rate = rate+f
		else:
			fin2=fin1
			break
	print "Case #" + str(cases+1) + ": " + str(fin2)
	out.write("Case #" + str(cases+1) + ": " + str(fin2) + "\n")
