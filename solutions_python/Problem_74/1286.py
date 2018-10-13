#!/usr/bin/env python
# encoding: utf-8
"""
problemA.py

Created by Chris Vaughn on 2011-05-07.
"""

import sys
import os


def main():
	if len(sys.argv) < 2 :
		exit()
	
	with open(sys.argv[1], 'r') as f:
 		test_cases = f.readline().rstrip()
		
		for x in range(int(test_cases)):
			sequence = f.readline().rstrip()
			result = process_sequence(sequence)
			print "Case #%d: %d" % (x+1, result)
	f.closed
	
def process_sequence(sequence):
	clock = 0
	orange_position = 1
	blue_position = 1

	seq = sequence.split(" ")
	buttons_remaining = total_remaining = int(seq[0])
	index = 0
	instructions = []
	orange_instr = []
	blue_instr = []
	
	while total_remaining != len(instructions):
		bot = seq[index+1]
		pos = seq[index+2]
		index = index+2
		instruction = [bot, pos]
		instructions.append(instruction)
		if bot == 'O':
			orange_instr.append(instruction)
		else:
			blue_instr.append(instruction)
	
	while len(instructions) > 0:
		current = instructions[0]

		my_next = None
		if len(orange_instr) > 0:
			my_next = orange_instr[0];
		(pos, pressed) = calculate_move(['O',orange_position], current, my_next)
		orange_position = pos
		if pressed == True:
			instructions.pop(0)
			orange_instr.pop(0)

		my_next = None
		if len(blue_instr) > 0:
			my_next = blue_instr[0];
		(pos, pressed) = calculate_move(['B',blue_position], current, my_next)
		blue_position = pos
		if pressed == True:
			instructions.pop(0)
			blue_instr.pop(0)
						
		clock = clock + 1
	return clock

def calculate_move(state, current_instr, next_instr):
	
	bot = state[0]
	pos = int(state[1])
	curr_bot = current_instr[0]
	curr_pos = int(current_instr[1])
	
	if next_instr is not None:
		next_bot = next_instr[0]
		next_pos = int(next_instr[1])

	pressed_button = False
	if bot == curr_bot:
		if pos == curr_pos:
			pressed_button = True
		elif pos < curr_pos:
			pos = pos + 1	
		elif pos > curr_pos:
			pos = pos - 1
	elif next_instr is not None:
		if pos < next_pos:
			pos = pos + 1	
		elif pos > next_pos:
			pos = pos - 1
	
	return (pos, pressed_button)
	
if __name__ == '__main__':
	main()

