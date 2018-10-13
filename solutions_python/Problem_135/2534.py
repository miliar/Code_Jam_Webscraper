T = input("")
f = [0]*4
s = [0]*4
for x in xrange(T):
	r1 = input("") - 1
	for i in xrange(4):
		f[i] = raw_input("").split()
	r2 = input("") - 1
	for i in xrange(4):
		s[i] = raw_input("").split()
	count = 0
	for i in range(4):
		for j in range(4):
			if f[r1][i] == s[r2][j]:
				count += 1
				num = i
	if count == 1:
		print "Case #" + str(x + 1) + ":", f[r1][num]
	elif count > 1:
		print "Case #" + str(x + 1) + ":", "Bad magician!"
	else:
		print "Case #" + str(x + 1) + ":", "Volunteer cheated!"