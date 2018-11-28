f = open('A-small-attempt0.in', 'r')
o = open('o.txt', 'w')
t = int(f.readline())

for i in range(t):
	z = 0
	brr = []
	while z < 2:
		z += 1
		arr = []
		x = 0
		b = int(f.readline())
		while x < 4:
			x += 1
			strsp = f.readline()
			arr.append(strsp.split())
		brr.append(arr[b-1])
		
	dr = 0
	sm = 0
	for a in brr[0]:
		for b in brr[1]:
			if a == b:
				dr = a
				sm += 1
	if sm == 1:
		gstr = "Case #" + str(i+1) + ": " + str(dr) + "\n"
	elif sm > 1:
		gstr = "Case #" + str(i+1) + ": Bad magician!\n"
	elif sm == 0:
		gstr = "Case #" + str(i+1) + ": Volunteer cheated!\n"
	print gstr
	o.write(gstr)
