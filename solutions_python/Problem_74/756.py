#!/usr/bin/env python3

import sys

# drop first line of stdin
sys.stdin.readline()

for test, line in enumerate(sys.stdin):
	seq_raw = line.split()[1:]
	seq = []
	orange_queue = []
	blue_queue = []
	for i in range(0, len(seq_raw), 2):
		color = seq_raw[i]
		button = int(seq_raw[i+1])
		seq.append((color, button))
		if color == 'B':
			blue_queue.append(button)
		elif color == 'O':
			orange_queue.append(button)
	time = 0
	next_button = None
	next_blue = None
	next_orange = None
	pos_blue = 1
	pos_orange = 1
	while True:
		if next_button is None:
			try:
				next_button = seq.pop(0)
			except IndexError:
				# no more buttons
				break
			if next_blue is None:
				try:
					next_blue = blue_queue.pop(0)
				except IndexError:
					pass
			if next_orange is None:
				try:
					next_orange = orange_queue.pop(0)
				except IndexError:
					pass
		# increment time
		time += 1
		# blue bot
		if next_blue is not None:
			if next_blue > pos_blue:
				pos_blue += 1
			elif next_blue < pos_blue:
				pos_blue -= 1
			else:
				if next_button is not None and next_button[0] == 'B':
					next_button = None
					next_blue = None
		# orange bot
		if next_orange is not None:
			if next_orange > pos_orange:
				pos_orange += 1
			elif next_orange < pos_orange:
				pos_orange -= 1
			else:
				if next_button is not None and next_button[0] == 'O':
					next_button = None
					next_orange = None
	print('Case #{}: {}'.format(test+1, time))
