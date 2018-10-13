#!/usr/bin/env python
def get_int_arr():
	return [int(x) for x in raw_input().split()]

def solve():
	time = 0
	orange = 1
	blue = 1
	vals = raw_input().split()

	N = int(vals.pop(0))
	command = [(vals[2*i], int(vals[2*i+1])) for i in range(N)]

	i = 0
	while i < N:
		done = False
		color, pos = command[i]
		# next opposite
		j = i+1
		pos2 = -1
		while j < N:
			if command[j][0] == color:
				j += 1
			else:
				pos2 = command[j][1]
				break
		if color == 'O':
			# move orange
			if orange < pos:
				orange += 1
			elif orange > pos:
				orange -= 1
			else:
				done = True
			# move blue
			if pos2 > 0:
				if blue < pos2:
					blue += 1
				elif blue > pos2:
					blue -= 1
		else:	# color = blue
			# move blue
			if blue < pos:
				blue += 1
			elif blue > pos:
				blue -= 1
			else:
				done = True
			if pos2 > 0:
				if orange < pos2:
					orange += 1
				elif orange > pos2:
					orange -= 1
		if done:
			i += 1
			
		time += 1
	return str(time)

t = get_int_arr()[0]
for x in range(t):
	print 'Case #%d: %s' % (x+1, solve())
