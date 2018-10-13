#!/usr/bin/python3

import sys, os, string, re

in_file = sys.stdin
out_file = sys.stdout

class Game:
	def __init__(self):
		self.winner_memo = {}
		self.loser_memo = {}

	def winner(self, a, b):
		if a < b:
			(a, b) = (b, a)
		if a == b:
			return False
		if a%b == 0:
			return True
		if (a, b) in self.winner_memo.keys():
			return self.winner_memo[(a, b)]
		k = a//b
		while k > 0:
			if self.loser(a-k*b, b):
				self.winner_memo[(a, b)] = True
				return True
			k -= 1
		self.winner_memo[(a, b)] = False
		return False
	
	def loser(self, a, b):
		if a < b:
			(a, b) = (b, a)
		if a == b:
			return True
		if a%b == 0:
			return False
		if (a, b) in self.loser_memo.keys():
			return self.loser_memo[(a, b)]
		k = a//b
		while k > 0:
			if not self.winner(a-k*b, b):
				self.loser_memo[(a, b)] = False
				return False
			k -= 1
		self.loser_memo[(a, b)] = True
		return True
	

T = int(in_file.readline())
for case_num in range(1, T+1):
	toks = in_file.readline().split()
	(A1, A2, B1, B2) = (int(toks[0]), int(toks[1]), int(toks[2]), int(toks[3]))

	game = Game()

	count = 0
	for a in range(A1, A2+1):
		for b in range(B1, B2+1):
			if game.winner(a, b):
				count += 1

	out_file.write('Case #%d: %d\n' % (case_num, count))
