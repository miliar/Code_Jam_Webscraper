#!/usr/bin/python

class Tic:

	PLAYER_ONE_MARK = 'X'
	PLAYER_TWO_MARK = 'O'
	WILD_MARK  = 'T'
	EMPTY_MARK = '.'

	PLAYER_ONE_WON = 1
	PLAYER_TWO_WON = 2
	DRAW_RESULT = 3
	GAME_NOT_COMPLETE = 4

	def __init__(self,input_lines):
		#print input_lines
		self.tic = [ [ i for i in line ] for line in input_lines ]
		#print self.tic
	
	def solve(self):
		
		PLAYER_ONE = 1
		PLAYER_TWO = 2
		PLAYER_NONE = 3
		PLAYER_WILD = 4
		PLAYER_NOT_INITED = 5

		curr_line_player = {}
		curr_column_player = {}
		reg_diag_player = PLAYER_NOT_INITED
		other_diag_player = PLAYER_NOT_INITED

		empty_found = False

		for i in xrange(len(self.tic)):
			#print "column: " + str(i)
			for j in xrange(len(self.tic[0])):
				#print "line: " + str(j)
				if self.tic[i][j] == self.EMPTY_MARK:
					empty_found = True

				if i == j:
					if reg_diag_player == PLAYER_NOT_INITED:
						if self.tic[i][j] == self.PLAYER_ONE_MARK:
							reg_diag_player = PLAYER_ONE
						elif self.tic[i][j] == self.PLAYER_TWO_MARK:
							reg_diag_player = PLAYER_TWO
						elif self.tic[i][j] == self.EMPTY_MARK:
							reg_diag_player = PLAYER_NONE
						elif self.tic[i][j] == self.WILD_MARK:
							reg_diag_player = PLAYER_WILD
					else:
						if reg_diag_player == PLAYER_ONE:
							if i == (len(self.tic) - 1):
								if self.tic[i][j] == self.PLAYER_ONE_MARK or self.tic[i][j] == self.WILD_MARK:
									return self.PLAYER_ONE_WON
							if self.tic[i][j] == self.PLAYER_TWO_MARK or self.tic[i][j] == self.EMPTY_MARK:
								reg_diag_player = PLAYER_NONE

						elif reg_diag_player == PLAYER_TWO:
							if i == (len(self.tic) - 1):
								if self.tic[i][j] == self.PLAYER_TWO_MARK or self.tic[i][j] == self.WILD_MARK:
									return self.PLAYER_TWO_WON
							if self.tic[i][j] == self.PLAYER_ONE_MARK or self.tic[i][j] == self.EMPTY_MARK:
								reg_diag_player = PLAYER_NONE

						elif reg_diag_player == PLAYER_WILD:
							if self.tic[i][j] == self.PLAYER_TWO_MARK:
								reg_diag_player = PLAYER_TWO
							elif self.tic[i][j] == self.PLAYER_ONE_MARK:
								reg_diag_player = PLAYER_ONE
							elif self.tic[i][j] == self.EMPTY_MARK:
								reg_diag_player = PLAYER_NONE


				if i == len(self.tic) - (j+1):
					if other_diag_player == PLAYER_NOT_INITED:
						if self.tic[i][j] == self.PLAYER_ONE_MARK:
							other_diag_player = PLAYER_ONE
						elif self.tic[i][j] == self.PLAYER_TWO_MARK:
							other_diag_player = PLAYER_TWO
						elif self.tic[i][j] == self.EMPTY_MARK:
							other_diag_player = PLAYER_NONE
						elif self.tic[i][j] == self.WILD_MARK:
							other_diag_player = PLAYER_WILD
					else:
						if other_diag_player == PLAYER_ONE:
							if i == (len(self.tic) - 1):
								if self.tic[i][j] == self.PLAYER_ONE_MARK or self.tic[i][j] == self.WILD_MARK:
									return self.PLAYER_ONE_WON
							if self.tic[i][j] == self.PLAYER_TWO_MARK or self.tic[i][j] == self.EMPTY_MARK:
								other_diag_player = PLAYER_NONE

						elif other_diag_player == PLAYER_TWO:
							if i == (len(self.tic) - 1):
								if self.tic[i][j] == self.PLAYER_TWO_MARK or self.tic[i][j] == self.WILD_MARK:
									return self.PLAYER_TWO_WON
							if self.tic[i][j] == self.PLAYER_ONE_MARK or self.tic[i][j] == self.EMPTY_MARK:
								other_diag_player = PLAYER_NONE

						elif other_diag_player == PLAYER_WILD:
							if self.tic[i][j] == self.PLAYER_TWO_MARK:
								other_diag_player = PLAYER_TWO
							elif self.tic[i][j] == self.PLAYER_ONE_MARK:
								other_diag_player = PLAYER_ONE
							elif self.tic[i][j] == self.EMPTY_MARK:
								other_diag_player = PLAYER_NONE


				if not i in curr_column_player:
					if self.tic[i][j] == self.PLAYER_ONE_MARK:
						curr_column_player[i] = PLAYER_ONE
					elif self.tic[i][j] == self.PLAYER_TWO_MARK:
						curr_column_player[i] = PLAYER_TWO
					elif self.tic[i][j] == self.EMPTY_MARK:
						curr_column_player[i] = PLAYER_NONE
					elif self.tic[i][j] == self.WILD_MARK:
						curr_column_player[i] = PLAYER_WILD
				else:
					if curr_column_player[i] == PLAYER_ONE:
						if j == (len(self.tic) - 1):
							if self.tic[i][j] == self.PLAYER_ONE_MARK or self.tic[i][j] == self.WILD_MARK:
								return self.PLAYER_ONE_WON
						if self.tic[i][j] == self.PLAYER_TWO_MARK or self.tic[i][j] == self.EMPTY_MARK:
							curr_column_player[i] = PLAYER_NONE

					elif curr_column_player[i] == PLAYER_TWO:
						if j == (len(self.tic) - 1):
							if self.tic[i][j] == self.PLAYER_TWO_MARK or self.tic[i][j] == self.WILD_MARK:
								return self.PLAYER_TWO_WON
						if self.tic[i][j] == self.PLAYER_ONE_MARK or self.tic[i][j] == self.EMPTY_MARK:
							curr_column_player[i] = PLAYER_NONE

					elif curr_column_player[i] == PLAYER_WILD:
						if self.tic[i][j] == self.PLAYER_TWO_MARK:
							curr_column_player[i] = PLAYER_TWO
						elif self.tic[i][j] == self.PLAYER_ONE_MARK:
							curr_column_player[i] = PLAYER_ONE
						elif self.tic[i][j] == self.EMPTY_MARK:
							curr_column_player[i] = PLAYER_NONE


				if not j in curr_line_player:
					if self.tic[i][j] == self.PLAYER_ONE_MARK:
						curr_line_player[j] = PLAYER_ONE
					elif self.tic[i][j] == self.PLAYER_TWO_MARK:
						curr_line_player[j] = PLAYER_TWO
					elif self.tic[i][j] == self.EMPTY_MARK:
						curr_line_player[j] = PLAYER_NONE
					elif self.tic[i][j] == self.WILD_MARK:
						curr_line_player[j] = PLAYER_WILD

				else:
					if curr_line_player[j] == PLAYER_ONE:
						if i == (len(self.tic) - 1):
							if self.tic[i][j] == self.PLAYER_ONE_MARK or self.tic[i][j] == self.WILD_MARK:
								return self.PLAYER_ONE_WON
						if self.tic[i][j] == self.PLAYER_TWO_MARK or self.tic[i][j] == self.EMPTY_MARK:
							curr_line_player[j] = PLAYER_NONE

					elif curr_line_player[j] == PLAYER_TWO:
						if i == (len(self.tic) - 1):
							if self.tic[i][j] == self.PLAYER_TWO_MARK or self.tic[i][j] == self.WILD_MARK:
								return self.PLAYER_TWO_WON
						if self.tic[i][j] == self.PLAYER_ONE_MARK or self.tic[i][j] == self.EMPTY_MARK:
							curr_line_player[j] = PLAYER_NONE

					elif curr_line_player[j] == PLAYER_WILD:
						if self.tic[i][j] == self.PLAYER_TWO_MARK:
							curr_line_player[j] = PLAYER_TWO
						elif self.tic[i][j] == self.PLAYER_ONE_MARK:
							curr_line_player[j] = PLAYER_ONE
						elif self.tic[i][j] == self.EMPTY_MARK:
							curr_line_player[j] = PLAYER_NONE
						

				#print reg_diag_player
				#print other_diag_player
				#print curr_line_player[j]
				#print curr_column_player[i]
		if empty_found:
			return self.GAME_NOT_COMPLETE
		else:
			return self.DRAW_RESULT



import sys
input_lines = open(sys.argv[1], "rt").readlines()
stripped_input_lines = [line.strip() for line in input_lines]
num_tests = int(input_lines[0])
#print num_tests

for i in xrange(num_tests):
	tic = Tic(stripped_input_lines[i*5+1:i*5+5])
	result =  tic.solve()
	if result == Tic.PLAYER_ONE_WON:
		print "Case #"+str(i+1)+": X won"
	if result == Tic.PLAYER_TWO_WON:
		print "Case #"+str(i+1)+": O won"
	if result == Tic.GAME_NOT_COMPLETE:
		print "Case #"+str(i+1)+": Game has not completed"
	if result == Tic.DRAW_RESULT:
		print "Case #"+str(i+1)+": Draw"
