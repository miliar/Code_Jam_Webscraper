#!/usr/bin/env python3
# These are my first python scripts, please bear with me
# Not much to say here, a recursive algorithm. It returns the number of
# valid words. First it tries to find a "(" character. If there is no
# parenthesis, then it is a full word, so check if the language contains
# it, and return 1 or 0. If we find parenthesis, then everything before it
# we call prefix, everything in it we call middle, and lets call everything
# after it postfix. Prefix cannot contain any parenthesis, so we check
# whether we can find a word from the language beginning with the prefix.
# If yes, we can continue, otherwise there is no point checking out other
# combinations.
# The first version didn't contain the prefix validity check, therefore
# it was extremely slow on the input data.

import sys

line = sys.stdin.readline().split()

# Number of characters in words:
L = int(line[0])
# Number of words in the language:
D = int(line[1])
# Number of test cases:
N = int(line[2])
# This set will store the whole language:
language = set()

for d in range(D):
	language.add(sys.stdin.readline().strip())

def prefix_in_language(prefix):
	l = len(prefix)
	for w in language:
		if w[:l] == prefix:
			return True
	return False

def solveword(word):
	sword = word.split("(", 1)
	if len(sword) == 1:
		# There is no parenthesis
		if word in language:
			#print(word, file=sys.stderr)
			return 1
		else:
			return 0
	elif len(sword) == 2:
		# There is parenthesis
		prefix = sword[0]
		if not prefix_in_language(prefix):
			return 0
		sword = sword[1].split(")", 1)
		middle = sword[0]
		postfix = sword[1]
		result = 0
		for m in middle:
			result += solveword(prefix + m + postfix)
		return result
	else:
		print("Something went wrong with len(sword)", file=sys.stderr)

def solvecase(n, line):
	result = solveword(line)
	print("Case #" + str(n) + ":", result)

for n in range(N):
	line = sys.stdin.readline().strip()
	solvecase(n+1, line)

