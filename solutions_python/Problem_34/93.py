# Author: Brian Armstrong
# Code Jam 2009
# Qualification Round
# Problem A: Alien Language

import sys, os

a_ref_ord = lambda x: ord(x) - ord('a') # return ord(x) referenced to 'a'

def nextchars(word):
	# Returns a list of the next character or characters possible in word
	# 	This list is a_ref_ord'd!
	# Also returns the remainder of the word
	if len(word) == 0:
		return ([], [])
	if word[0] == '(':
		chars = []
		n = 1
		while word[n] != ')':
			chars.append(a_ref_ord(word[n]))
			n = n + 1
		return (chars, word[n+1:])
	return ([a_ref_ord(word[0])], word[1:])

class TokenNode(object):
	def __init__(self):
		self.nodes = [None] * 26
	def insert(self, word):
		if len(word) == 0:
			return
		first = a_ref_ord(word[0])
		if self.nodes[first] is None:
			self.nodes[first] = TokenNode()
		self.nodes[first].insert(word[1:])
	def find(self, case):
		if len(case) == 0:
			return 1
		(chars, remainder) = nextchars(case)
		n = 0
		for char in chars:
			if self.nodes[char] is not None:
				n = n + self.nodes[char].find(remainder)

		return n


class WordTree(object):
	# Root node of a tree of tokens
	# Each node contains a list of nodes
	def __init__(self):
		self.nodes = [None] * 26
	def insert(self, word):
		first = a_ref_ord(word[0])
		if self.nodes[first] is None:
			self.nodes[first] = TokenNode()
		self.nodes[first].insert(word[1:])
	def find(self, case):
		(chars, remainder) = nextchars(case)
		n = 0
		for char in chars:
			if self.nodes[char] is not None:
				n = n + self.nodes[char].find(remainder)
		return n	

def print_cases(cases):
	n = 1
	for case in cases:
		print "Case #" + str(n) + ": " + str(case)
		n = n + 1

def main():
	args = sys.stdin.readline().split()
	if len(args) == 3:
		input_l = int(args[0]) # used?
		input_d = int(args[1])
		input_n = int(args[2])
		cases = []

		wtree = WordTree()
		for d in range(0, input_d):
			word = sys.stdin.readline().rstrip()
			wtree.insert(word)

		for n in range(0, input_n):
			case = sys.stdin.readline().rstrip()
			cases.append(wtree.find(case))

		print_cases(cases)

	else:
		print "Invalid number of arguments."

if __name__ == "__main__":
	main()
