#!/usr/bin/python

###
# Definitions and files to open
###
import random

out_array = []
source_file = 'Q1.txt'

try:
	f = open(source_file)
except IOError:
	print ('could not open source file ' + source_file)

###
# Classes we need
###

class game:
	def __init__(self, num, str_array):
		self.num = num
		self.str_array = str_array
		self.game_str_array = []
		self.result_num = 0
		self.result = ''

		for ii in range(num):
			self.game_str_array.append(game_string(str_array[ii]))

		self.canonical_str = self.game_str_array[0].sample_str
		self.num_letters = len(self.canonical_str)

		felga = self.felga_won()
		if not felga:
			for ii in range(self.num_letters):
				num_array = []
				for jj in range(self.num):
					num_array.append(self.game_str_array[jj].rep_array[ii])
				# Okay so we have an array of the number of reps each string have
				# of the jjth letter...
				num_array.sort()
				if (len(num_array)%2) == 1:
					pivot_ix = int((len(num_array) - 1)/2)
				else:
					pivot_ix = int(len(num_array)/2)
				pivot = num_array[pivot_ix]
				for jj in range(self.num):
					self.result_num += abs(num_array[jj] - pivot)
			self.result = str(self.result_num)
		return

	def felga_won(self):
		for ii in range(1, self.num):
			if self.game_str_array[ii].sample_str != self.canonical_str:
				self.result = 'Fegla Won'
				return True
		return False

class game_string:
	def __init__(self, string):
		self.string = string
		self.sample_str = ''
		self.rep_array = []
		ch = ''
		jj = -1
		for ii in range(len(string)):
			if string[ii] != ch:
				# Get the canonical string
				self.rep_array.append(0)
				jj += 1
				self.rep_array[jj] += 1
				ch = string[ii]
				self.sample_str += ch
			else:
				# Add 1 to the number of times this char is repeated
				self.rep_array[jj] += 1

###
# Parse the source file and play the games.
###

num_games = int(f.readline().rstrip())

for ii in range(num_games):
	# Parse a single game here
	input_str_array = []
	input_num = int(f.readline().rstrip())
	for jj in range(input_num):
		input_str_array.append(str(f.readline().rstrip()))
	
	# Play the game and get the result
	current_game = game(input_num, input_str_array)
	out_array.append('Case #' + str(ii + 1) + ': ' + current_game.result)

###
# Print out the results of all the games
###

for out_line in out_array:
	print(out_line)
