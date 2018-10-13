# -*- coding: utf-8 -*-

import sys
import os.path
import os, time, itertools

INITIAL_HEIGHT=100

class Sample:
	def solve(self,board,row_size,col_size):
		self.board = board
		return "YES" if self.judge(row_size,col_size) else "NO"

	def judge(self,row_size,col_size):
		cut_config_of_row = [INITIAL_HEIGHT] * row_size
		cut_config_of_col = [INITIAL_HEIGHT] * col_size
		
		for i in range(row_size):		
			mix_flg=False	
			tmp_max=max(self.board[i])

			if cut_config_of_row[i]!=INITIAL_HEIGHT and cut_config_of_row[i]!=tmp_max:
				return false

			cut_config_of_row[i]=tmp_max

			for j in range(col_size):
				if self.board[i][j]!=tmp_max:
					mix_flg=True
					break
			
			if mix_flg:
				for j in range(col_size):
					if self.board[i][j]!=tmp_max:
						if cut_config_of_col[j]==INITIAL_HEIGHT:						
							cut_config_of_col[j]=self.board[i][j]
						elif cut_config_of_col[j]!=self.board[i][j]:
							return False

			else:
				for j in range(col_size):
					if cut_config_of_col[j]<tmp_max:
						return False


		for j in range(col_size):
			mix_flg=False
			
			tmp_max=-1
			for i in range(row_size):
				if self.board[i][j]>tmp_max:
					tmp_max=self.board[i][j]
			
			if cut_config_of_col[j]!=INITIAL_HEIGHT and cut_config_of_col[j]!=tmp_max:
				return False

			cut_config_of_col[j]=tmp_max

			for i in range(row_size):
				if self.board[i][j]!=tmp_max:
					mix_flg=True
					break
			
			if mix_flg:
				for i in range(row_size):
					if self.board[i][j]!=tmp_max:
						if cut_config_of_row[i]==INITIAL_HEIGHT:						
							cut_config_of_row[i]=self.board[i][j]
						elif cut_config_of_row[i]!=self.board[i][j]:
							return False

			else:
				for i in range(row_size):
					if cut_config_of_row[i]<tmp_max:
						return False

		return True

def read_nums():
	return map(int, in_fh.readline().split())
def read_str():
	return in_fh.readline().rstrip('\r\n')

def read_testcase():
	n,m = read_nums()
	board=[]
	for i in range(n):
		board.append(read_nums())
	print board
	print "-----"
	return {'board':board,'row_size':n,'col_size':m}

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
