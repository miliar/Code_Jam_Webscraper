base = 2**40
fp = open("in.txt")
T = int(fp.readline())

for i in range(T):
	lay = 1
	line = fp.readline()
	a = line.split("/")
	P = int(a[0])
	Q = int(a[1])
	if P == 0 or P == Q:
		print "Case #%s: 0" %(i+1)
	#yuefen
	while P % 2 == 0 and Q % 2 == 0:
		P = P / 2
		Q = Q / 2

	while Q != 1:
		if Q % 2 == 0:
			Q = Q / 2
			if P < Q:
				lay += 1
		else:
			if P % Q == 0:
				Q = Q / P
			else:
				print "Case #%s: impossible" %(i+1)
				break
	else:
		print "Case #%s: %s" %(i+1, lay)