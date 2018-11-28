from sys import stdin
t = int(stdin.readline())
for case in xrange(t):
	row = int(stdin.readline())
	a = []
	fir = stdin.readline()
	sec = stdin.readline()
	thi = stdin.readline()
	four = stdin.readline()
	a.append(fir)
	a.append(sec)
	a.append(thi)
	a.append(four)
	gr = set()
	tar = a[row-1]
	tar = tar.split()
	gr = set(tar)
	row = int(stdin.readline())
	a = []
	fir = stdin.readline()
	sec = stdin.readline()
	thi = stdin.readline()
	four = stdin.readline()
	a.append(fir)
	a.append(sec)
	a.append(thi)
	a.append(four)
	tar = a[row-1]
	tar = tar.split()
	tr = set(tar)
	valid = 0
	ans = 3
	for x in tr:
		if x in gr:
			valid+=1
			ans = x
	#print valid
	res = ""
	if valid == 0:
		res = "Volunteer cheated!"
	elif valid == 1:
		res = ans
	else:
		res = "Bad magician!"
	print "Case #%d:"%(case+1), res
	
	
	