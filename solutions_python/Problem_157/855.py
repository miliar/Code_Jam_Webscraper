def mult(a, b):
	#positives
	if a == '1':
		return b
	if a == 'i':
		if b == 'i':
			return '-1'
		elif b == 'j':
			return 'k'
		elif b == 'k':
			return '-j'
	if a == 'j':
		if b == 'i':
			return '-k'
		elif b == 'j':
			return '-1'
		elif b == 'k':
			return 'i'
	if a == 'k':
		if b == 'i':
			return 'j'
		if b == 'j':
			return '-i'
		if b == 'k':
			return '-1'

	#negatives
	
	if a == '-1':
		return '-' + b
	if a == '-i':
		if b == 'i':
			return '1'
		elif b == 'j':
			return '-k'
		elif b == 'k':
			return 'j'
	if a == '-j':
		if b == 'i':
			return 'k'
		elif b == 'j':
			return '1'
		elif b == 'k':
			return '-i'
	if a == '-k':
		if b == 'i':
			return '-j'
		if b == 'j':
			return 'i'
		if b == 'k':
			return '1'	



for t in range(0, int(input())):
	l, x = [int(x) for x in input().split()]
	cha = list(input())
	cha = cha * x

	goal = ['i', 'j', 'k']
	step = 0
	result = ''
	if cha == goal:
		result = 'ijk'
		cha = []
	else:
		while(True):
			if len(cha) < 2:
				break
			a = cha.pop(0)
			b = cha.pop(0)
			m = mult(a, b)
			if m == goal[step]:
				if step < 2:
					step += 1
					result += m
				else:
					if len(cha) < 2:
						result += m
					else:
						cha.insert(0, m)

			else:
				cha.insert(0, m)

	if result == 'ijk' and len(cha) == 0:
		print("Case #%d: YES" %(t+1))
	else:
		print("Case #%d: NO" %(t+1))