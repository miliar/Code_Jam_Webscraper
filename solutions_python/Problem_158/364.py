T = int(raw_input())
f = open('out.txt', 'w')
cas = 0
while T > 0:
	T -= 1
	cas += 1
	x, r, c = map(int, raw_input().split())
	f.write("Case #" + str(cas) + ": ")
	if x >= 7:
		f.write("RICHARD")
	elif r * c % x != 0:
		f.write("RICHARD")
	elif x == 1:
		f.write("GABRIEL")
	elif x == 2:
		f.write("GABRIEL")
	elif x == 3:
		if min(r, c) == 1:
			f.write("RICHARD")
		else:
			f.write("GABRIEL")
	elif x == 4:
		if min(r, c) <= 2:
			f.write("RICHARD")
		else:
			f.write("GABRIEL")
	elif x == 5:
		if min(r, c) <= 3:
			f.write("RICHARD")
		else:
			f.write("GABRIEL")
	else:
		if min(r, c) <= 3:
			f.write("RICHARD")
		else:
			f.write("GABRIEL")

	f.write('\n')