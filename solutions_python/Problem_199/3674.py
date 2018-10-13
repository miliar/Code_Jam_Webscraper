def flip(pancake):
	if pancake == 0:
		return 1
	elif pancake == 1:
		return 0
	else:
		return ''
f = open('A-large.in', 'r')
T = int(f.readline())
for i in range(T):
	count = 0
	pancakes_int = []
	line = f.readline().rsplit()
	pancakes = line[0]
	for pancake in pancakes:
		if pancake == '-':
			pancakes_int.append(0)
		elif pancake == '+':
			pancakes_int.append(1)
	pan = int(line[1])
	for j in range(len(pancakes_int)-pan+1):
		if pancakes_int[j] == 0:
			count = count+1
			for k in range(pan):
				pancakes_int[j+k] = flip(pancakes_int[j+k])

	if 0 in pancakes_int:
		print 'Case #' + str(i+1) + ': IMPOSSIBLE'
	else:
		print 'Case #' + str(i+1) + ': ' + str(count)