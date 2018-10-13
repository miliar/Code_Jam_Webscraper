# -*- coding:utf-8 -*-

fr = open("B-large.in","r")
fw = open("B-large.out","w")
lines  = int(fr.readline())
i = 1

while i<=lines:
	#Problem Start	
	l = fr.readline()
	s = l.split()
	C = float(s[0])
	F = float(s[1])
	X = float(s[2])
	
	CS = 2.0 # initial cookie /second
	R  = 0.0 # Result

	while True:
		if (((X-C)*F)/C) <= CS:
			break
		R = R + (C/CS)
		CS= CS + F
	R = R + (X/CS)	
	
	fw.write("Case #{}: {}\n".format(i,R))
	#End
	i=i+1

fr.close
fw.close