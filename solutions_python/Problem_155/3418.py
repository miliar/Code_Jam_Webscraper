with open('input.in', 'r') as f, open('output', 'w') as w:
	cases = f.readline()
	print(cases)
	for c in range(int(cases)):
		shyness, audience = f.readline().split(' ')
		standing = 0
		invited = 0
		for i,a in enumerate(audience):
			if a == '\n':
				continue
			people = int(a)
			if people == 0:
				continue
			if i <= standing:
				standing += people
			else:
				invited += i - standing
				standing += people + invited
			if standing >= int(shyness):
				break
		w.write('Case #' + str(c+1) + ': ' + str(invited) + '\n')
		print('Case #' + str(c+1) + ': ' + str(invited) + ' ' + shyness + ' ' + audience[:-1])