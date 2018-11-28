f = open('1-small')
out = open('out', 'w')
t = f.readline()
case = 1
for line in f:
	curr = 0
	friends = 0
	(smax, people) = line.strip().split(' ')
	for i, c in enumerate(people):
		n = int(c)
		if i > curr:
			friends = friends + i - curr
			curr = i
		curr = curr + n
	out.write('Case #' + str(case) + ': ' + str(friends) + '\n')
	case = case + 1
out.close()
