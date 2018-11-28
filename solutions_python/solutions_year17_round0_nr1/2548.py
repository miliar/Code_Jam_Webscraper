#!/usr/bin/python3

lines = int(input())

for attempt in range(1,lines+1):

	line = input()
	SK = line.split()
	pancakes = SK[0]
	width = int(SK[1])

	flips = 0

	flipped = {'-':'+', '+':'-'}

	while True:
		pancakes = pancakes.strip('+')
		if not pancakes:
			break
		if len(pancakes) < width and '-' in pancakes:
			flips = -1
			break
		#print('preflip:',pancakes)
		for i in range(width):
			pancakes = pancakes[:i] + flipped[pancakes[i]] + pancakes[i+1:]
		#print('postflip:',pancakes)
		flips += 1

	if flips == -1:
		print('Case #' + str(attempt) + ': ' + 'IMPOSSIBLE')
	else:
		print('Case #' + str(attempt) + ': ' + str(flips))
