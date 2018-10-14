#!/usr/bin/python

# read number of test cases T
num_cases = int(raw_input())

class Robot:
	def __init__(self, name, moves):
		self.name = name
		self.current_pos = 1
		self.current_move = 0
		self.moves = moves
		if len(self.moves) > 0:
			self.next_pos = self.moves[self.current_move]
		else:
			self.next_pos = self.current_pos

	def move(self, time):
		#old_pos = self.current_pos
		if self.current_pos != self.next_pos:
			distance = abs(self.next_pos - self.current_pos)
			distance = min(time, distance)
			if self.next_pos > self.current_pos:
				self.current_pos += distance
			else:
				self.current_pos -= distance
		#if self.current_pos != old_pos:
		#	print("%s moved from %d to %d" % (self.name, old_pos, self.current_pos))
		#else:
		# print("%s did not move" % (self.name))

	def next_move(self):
		#print("%s pressed button %d" % (self.name, self.moves[self.current_move]))
		if self.current_move + 1 < len(self.moves):
			self.current_move += 1
			self.next_pos = self.moves[self.current_move] 
	
	def time_to_move(self):
		return abs(self.next_pos - self.current_pos)

for i in range(0, num_cases):
	terms = raw_input().split(' ')
	num_terms = int(terms[0])
	
	blue_moves   = []
	orange_moves = []
	moves        = []
	for j in range(0, num_terms):
		robot  = terms[2 * j + 1]
		button = int(terms[2 * j + 2]) 	
		if robot == 'B':
			moves.append('B')
			blue_moves.append(button)
		else:
			moves.append('O')
			orange_moves.append(button)
	
	blue = Robot("Blue", blue_moves)
	orange = Robot("Orange", orange_moves)
	#print(blue_moves)
	#print(orange_moves)	
	current_time = 0
	for current in range(0, len(moves)):
		#print("Current time: %d" % (current_time))
		if moves[current] == 'B':
			time = blue.time_to_move()
			blue.move(time)
			orange.move(time + 1)
			current_time += time + 1
			blue.next_move()
		else:
			time = orange.time_to_move()
			orange.move(time)
			blue.move(time + 1)
			current_time += time + 1
			orange.next_move()
	print("Case #%d: %d" % (i + 1, current_time))
	#print("\n")
