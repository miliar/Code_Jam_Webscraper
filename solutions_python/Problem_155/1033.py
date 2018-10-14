f = open('A-large.in')
lines = [s.strip() for s in f.readlines()]
o = open('output.dat', 'w')

i = 0
for line in lines[1:]:
	i = i + 1
	_, shyness = line.split(" ")

	s = 0
	m = 0
	for ix, el in enumerate(shyness):
		intel = int(el)
		if ix - s > m:
			m = ix - s
		s = s + intel
	print >>o, "Case #" + str(i) + ": " + str(m)
	