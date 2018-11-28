f = open("B-large.in")
g = open("resultado.txt", 'w')
f.readline()
i = 1
for line in f:
	line = line.strip()
	line = line.split()
	num_googlers = line[0]
	num_surprising = int(line[1])
	minimum = int(line[2])
	notes = line[3:]
	aux = 0
	if minimum == 1:
		min_normal = int(minimum) + (int(minimum) - 1) + (int(minimum) - 1)
		min_surprising = min_normal
	elif minimum == 0:
		min_normal = 0
		min_surprising = 0
	else:
		min_normal = int(minimum) + (int(minimum) - 1) + (int(minimum) - 1)
		min_surprising = int(minimum) + (int(minimum) - 2) + (int(minimum) - 2)
	for note in notes:
		if int(note) >= min_normal:
			aux += 1
		elif int(note) >= min_surprising and num_surprising > 0:
			aux += 1
			num_surprising -= 1
	g.write("Case #%s: %s \n" % (i, aux))
	i += 1