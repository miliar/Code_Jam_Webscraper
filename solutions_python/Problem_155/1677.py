limit = input()
people = []
for i in range(0, limit):
	inp = raw_input()
	people.append(map(str, inp.split(' ')))

cnt = 0
for i in people:
	cnt += 1
	sum = 0
	needed = 0
	for j in range(0, len(i[1])):
		if j == 0:
			sum += int(i[1][j])
		else:
			if sum + needed < j:
				needed += j - sum - needed
			sum += int(i[1][j])
	print 'Case #{}: {}'.format(cnt, needed)