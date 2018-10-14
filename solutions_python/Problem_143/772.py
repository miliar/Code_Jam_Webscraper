t = input()
times = 0
while times<t:
	total = 0
	abk = raw_input()
	abkl = abk.split()
	a = int(abkl[0])
	b = int(abkl[1])
	c = int(abkl[2])
	#ab = bin(a)
	#bb = bin(b)
	i = 0
	
	while i<a:
		i2 = 0
		while i2<b:
			#ii = bin(i)
			#i22 = bin(i2)
			r = i & i2
			if r<c:
				total = total+1
			i2 = i2+1
		i = i+1
	times = times+1
	timesstr = str(times)
	totalstr = str(total)
	print 'Case #'+timesstr+': '+totalstr 