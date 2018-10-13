# -*- coding: utf-8 -*-

import sys
import os.path
import os, time, itertools

BOARD_SIZE=4

class Sample:
	def solve(self,board):
		self.board = board

		# check goal
		winner = self.check_winner()
		if winner == 1:
			ans="X won"
		elif winner == -1:
			ans="O won"
		# check emptiness
		elif self.isFinished():
			ans="Draw"
		else:
			ans="Game has not completed"
				
		return ans

	def check_winner(self):
		#row
		for i in range(BOARD_SIZE):
			x_flg=True
			o_flg=True
			for j in range(BOARD_SIZE):
				elem = self.board[i][j]
				if elem==2:
					x_flg=False
					o_flg=False
					break
				elif elem==1:
					o_flg=False
				elif elem==-1:
					x_flg=False
			if x_flg:
				return 1
			elif o_flg:
				return -1

		#col
		for i in range(BOARD_SIZE):
			x_flg=True
			o_flg=True
			for j in range(BOARD_SIZE):
				elem = self.board[j][i]
				if elem==2:
					x_flg=False
					o_flg=False
					break
				elif elem==1:
					o_flg=False
				elif elem==-1:
					x_flg=False
			if x_flg:
				return 1
			elif o_flg:
				return -1
		
		#diagonal(1)
		x_flg=True
		o_flg=True
		for i in range(BOARD_SIZE):
			elem = self.board[i][i]
			if elem==2:
				x_flg=False
				o_flg=False
				break
			elif elem==1:
				o_flg=False
			elif elem==-1:
				x_flg=False
				
		if x_flg:
			return 1
		elif o_flg:
			return -1

		#diagonal(2)
		x_flg=True
		o_flg=True
		for i in range(BOARD_SIZE):
			elem = self.board[i][3-i]
			if elem==2:
				x_flg=False
				o_flg=False
				break
			elif elem==1:
				o_flg=False
			elif elem==-1:
				x_flg=False
		if x_flg:
			return 1
		elif o_flg:
			return -1

		return 0

	def isFinished(self):
		for i in range(BOARD_SIZE):
			for j in range(BOARD_SIZE):	
				if self.board[i][j]==2:
					return False
		return True

def read_nums():
	return map(int, in_fh.readline().split())
def read_str():
	return in_fh.readline().rstrip('\r\n')

def convert(ch):
	if ch=='X':
		ret=1
	elif ch=='O':
		ret=-1
	elif ch=='T':
		ret=0
	elif ch=='.':
		ret=2
	return int(ret)

def read_testcase():
	board=[]
	for i in range(BOARD_SIZE):
		board.append(map(convert,read_str()))
	#print board
	#print "-----"
	foo = read_str()
	return {'board':board}

def read_testcases(test_num):
	for i in range(test_num):
		yield read_testcase()

def wrapper_of_solve(q):
	sample=Sample()
	return sample.solve(**q)

if __name__ == '__main__':

	input_name = sys.argv[1]
	root, ext = os.path.splitext(input_name)
	in_fh=open(input_name)

	test_num=int(in_fh.readline())

	output_name = root + ".out"
	out_fhs=[open(output_name,'w')]

	testcases = read_testcases(test_num)

	mul_iter = itertools.imap(wrapper_of_solve, testcases)

	for (i, r) in enumerate(mul_iter, start=1):
	    for f in out_fhs:
	        print >> f, "Case #%d: %s" % (i, str(r))
