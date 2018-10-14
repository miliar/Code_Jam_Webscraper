#!/usr/bin/python
import sys

def solve(test_case):
	count = 1
	move_list = []
	o_move = []
	b_move = []
	while (1):
		try:
			button = int(test_case[count + 1])
			robot = test_case[count]
			count += 2
		except IndexError:
			break
		move_list.append((robot, button))
		if robot == 'O':
			o_move.append(button)
		else:
			b_move.append(button)
	time = 0
	o_count = 0
	o_pos = 1
	b_count = 0
	b_pos = 1
	move_count = 0
	while (1):
		time += 1
		flag = True

		if len(o_move) > 0 and o_count < len(o_move):
			if o_pos == o_move[o_count]:
				if move_list[move_count][0] == 'O':
					move_count += 1
					o_count += 1
					flag = False
					if move_count == len(move_list):
						break
			elif o_pos > o_move[o_count]:
				o_pos -= 1
			else:
				o_pos += 1

		if len(b_move) > 0 and b_count < len(b_move):
			if b_pos == b_move[b_count]:
				if move_list[move_count][0] == 'B' and flag:
					move_count += 1;
					b_count += 1
					if move_count == len(move_list):
						break
			elif b_pos > b_move[b_count]:
				b_pos -= 1
			else:
				b_pos += 1

		#print time, o_pos, o_count, b_pos, b_count
	#print test_case
	#print move_list, move_count
	#print o_count, o_move
	#print b_count, b_move
	return time

"""
def solve(test_case):
	count = 1
	o_pos = 1
	b_pos = 1
	time = 0
	last_b = time
	last_o = time
	prev_robot = 'x'
	while (1):
		try:
			button = int(test_case[count + 1])
			robot = test_case[count]
			count += 2
		except IndexError:
			break

		if robot == 'O':
			if prev_robot == 'B':
				if o_pos < button:
					o_pos += time - last_o
					if o_pos > button:
						o_pos = button
				if o_pos > button:
					o_pos -= time - last_o
					if o_pos < button:
						o_pos = button
			print 'o', o_pos, button, time
			last_o = time
			time += abs(button - o_pos) + 1
			o_pos = button
			print 'o', o_pos, button, time
		else:
			if prev_robot == 'O':
				if b_pos < button:
					b_pos += time - last_b
					if b_pos > button:
						b_pos = button
				if b_pos > button:
					b_pos -= time - last_b
					if b_pos < button:
						b_pos = button
			print 'b', b_pos, button, time
			last_b = time
			time += abs(button - b_pos) + 1
			b_pos = button
			print 'b', b_pos, button, time
		prev_robot = robot
	return time
"""

#Main script---------------------------------------------------------
def main():
	if len(sys.argv) != 2:
		sys.stderr.write("usage: %(self)s 'input'\n"%\
							{'self': sys.argv[0]})
		return

	count = 1
	try:
		f = open(sys.argv[1], 'r')
		for line in f:
			if len(line.split()) == 1:
				continue;
			sys.stdout.write('Case #' + str(count) + ': ' + str(solve(line.split())) + "\n")
			count += 1
	finally:
		f.close()
		 

if (__name__ == "__main__"):
	main()