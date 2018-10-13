# -*- coding:utf-8 -*-

f = open("A-small-attempt0.in","r")
lines = int(f.readline())
i = 1

while i<=lines:
	#Problem Start

	#first answer
	a = []
	row = int(f.readline())
	for j in range(1,5):
		l = f.readline()
		if j != row:
			continue
		s = l.split()
		a.append(int(s[0]))
		a.append(int(s[1]))
		a.append(int(s[2]))
		a.append(int(s[3]))

	#second answer
	b = []
	row = int(f.readline())
	for j in range(1,5):
		l = f.readline()
		if j != row:
			continue
		s = l.split()
		b.append(int(s[0]))
		b.append(int(s[1]))
		b.append(int(s[2]))
		b.append(int(s[3]))
	
	result = []
	for j in a:
		for k in b:
			if j == k:
				result.append(j)

	rlen = len(result)
	if rlen == 1:
		print ("Case #{}: {}".format(i,result[0]))
	elif rlen > 1:
		print ("Case #{}: Bad magician!".format(i))
	else:
		print ("Case #{}: Volunteer cheated!".format(i))

	#End
	i=i+1

f.close