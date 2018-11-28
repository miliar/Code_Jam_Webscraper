def arrage(n, unicorns):
	colors = [['R', 0], ['Y', 0], ['B', 0]]
	for key in unicorns:
		if key == 'R':
			colors[0][1] += unicorns[key]
		elif key == 'O':
			colors[0][1] += unicorns[key]
			colors[1][1] += unicorns[key]
		elif key == 'Y':
			colors[1][1] += unicorns[key]
		elif key == 'G':
			colors[1][1] += unicorns[key]
			colors[2][1] += unicorns[key]
		elif key == 'B':
			colors[2][1] += unicorns[key]
		else:
			colors[0][1] += unicorns[key]
			colors[2][1] += unicorns[key]

	colors.sort(key=lambda tup: tup[1], reverse=True)
	if 2 * colors[0][1] > n:
		return 'IMPOSSIBLE'

	arragement = []
	for i in range(n):
		arragement.append([])

	for i in range(0, 2 * colors[0][1], 2):
		arragement[i].append(colors[0][0])
	unicorns[colors[0][0]] = 0

	for i in range(n - 1, n - 2 * unicorns[colors[1][0]], -2):
		if arragement[i]:
			arragement[i - 1].append(colors[1][0])
		else:
			arragement[i].append(colors[1][0])
	unicorns[colors[1][0]] = 0

	if colors[1][0] == 'R':
		for i in range(0, 2 * unicorns['O'], 2):
			if arragement[i] == 'Y':
				arragement[i].append('R')
				unicorns['O'] -= 1
			else:
				arragement[i + 1].append('R')
		for i in range(2 * unicorns['O'], 2 * unicorns['O'] + 2 * unicorns['V'], 2):
			if arragement[i] == 'B':
				arragement[i].append('R')
				unicorns['V'] -= 1
			else:
				arragement[i + 1].append('R')
	elif colors[1][0] == 'Y':
		for i in range(0, 2 * unicorns['O'], 2):
			if arragement[i] == 'R':
				arragement[i].append('Y')
				unicorns['O'] -= 1
			else:
				arragement[i + 1].append('Y')
		for i in range(2 * unicorns['O'], 2 * unicorns['O'] + 2 * unicorns['G'], 2):
			if arragement[i] == 'B':
				arragement[i].append('Y')
				unicorns['G'] -= 1
			else:
				arragement[i + 1].append('Y')
	elif colors[1][0] == 'B':
		for i in range(0, 2 * unicorns['G'], 2):
			if arragement[i] == 'Y':
				arragement[i].append('B')
				unicorns['G'] -= 1
			else:
				arragement[i + 1].append('B')
		for i in range(2 * unicorns['G'], 2 * unicorns['G'] + 2 * unicorns['V'], 2):
			if arragement[i] == 'R':
				arragement[i].append('B')
				unicorns['V'] -= 1
			else:
				arragement[i + 1].append('B')

	for i in range(n):
		if not arragement[i]:
			arragement[i].append(colors[2][0])
			unicorns[colors[2][0]] -= 1

	i = 0
	while i < n:
		if colors[2][0] == 'R':
			if arragement[i][0] == 'R':
				i += 1
			elif arragement[i][0] == 'Y' and unicorns['O'] > 0 and (i == n - 1 or arragement[i + 1][0] != 'R'):
				arragement[i].append('R')
				unicorns['O'] -= 1
				i += 1
			elif arragement[i][0] == 'V' and unicorns['B'] > 0 and (i == n - 1 or arragement[i + 1][0] != 'R'):
				arragement[i].append('R')
				unicorns['B'] -= 1
				i += 1
		elif colors[2][0] == 'Y':
			if arragement[i][0] == 'Y':
				i += 1
			elif arragement[i][0] == 'R' and unicorns['O'] > 0 and (i == n - 1 or arragement[i + 1][0] != 'Y'):
				arragement[i].append('Y')
				unicorns['O'] -= 1
				i += 1
			elif arragement[i][0] == 'B' and unicorns['G'] > 0 and (i == n - 1 or arragement[i + 1][0] != 'Y'):
				arragement[i].append('Y')
				unicorns['G'] -= 1
				i += 1
		elif colors[2][0] == 'B':
			if arragement[i][0] == 'B':
				i += 1
			elif arragement[i][0] == 'Y' and unicorns['G'] > 0 and (i == n - 1 or arragement[i + 1][0] != 'B'):
				arragement[i].append('B')
				unicorns['G'] -= 1
				i += 1
			elif arragement[i][0] == 'R' and unicorns['V'] > 0 and (i == n - 1 or arragement[i + 1][0] != 'B'):
				arragement[i].append('B')
				unicorns['V'] -= 1
				i += 1
		i += 1

	for i in range(n):
		if 'R' in arragement[i] and 'Y' in arragement[i]:
			arragement[i] = 'O'
		elif 'Y' in arragement[i] and 'B' in arragement[i]:
			arragement[i] = 'G'
		elif 'R' in arragement[i] and 'B' in arragement[i]:
			arragement[i] = 'V'

	arragement = [color[0] for color in arragement]
	return ''.join(arragement)

T = int(input())
for i in range(T):
	params = [int(p) for p in input().split()]
	n = params[0]
	unicorns = {'R': params[1], 'O': params[2], 'Y': params[3], 'G': params[4],  'B': params[5],'V': params[6]}
	print('Case #{}: {}'.format(i + 1, arrage(n, unicorns)))