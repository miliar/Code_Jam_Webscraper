#!/usr/bin/env python

from __future__ import print_function
import sys

def tokenize(f, delim = [ ' ', '\n' ]):
	token = list()

	while True:
		ch = f.read(1)
		if ch == '':
			yield ''.join(token)
			raise StopIteration
			token = list()
		elif ch in delim:
			yield ''.join(token)
			token = list()
		else:
			token.append(ch)

def add_recipe(recipes, in1, in2, out):
	if in1 not in recipes:
		recipes[in1] = dict()
	if in2 not in recipes:
		recipes[in2] = dict()

	recipes[in1][in2] = out
	recipes[in2][in1] = out

def get_recipe(recipes, in1, in2):
	if in1 in recipes and in2 in recipes[in1]:
		return recipes[in1][in2]
	else:
		return False

def invoke(combos, destruct, inv):
	stack = list()

	for ch in inv:
		stack.append(ch)

		# combine the last two elements
		if len(stack) >= 2:
			combo = get_recipe(combos, stack[-1], stack[-2])
			if combo:
				stack.pop()
				stack.pop()
				stack.append(combo)

		# check if there are two opposed elements
		if len(stack) >= 1: 
			for ele in stack[:-1]:
				if get_recipe(destruct, ele, stack[-1]):
					stack = list()
					break
	return stack

tokens  = tokenize(sys.stdin)

T = int(tokens.next())
for t in xrange(0, T):
	tokens   = tokenize(sys.stdin)
	combos   = dict()
	destruct = dict()

	# combo recipes
	C  = int(tokens.next())
	if C > 0:
		for c in xrange(0, C):
			[ in1, in2, out ] = tokens.next()
			add_recipe(combos, in1, in2, out)

	# oppose recipes
	D  = int(tokens.next())
	if D > 0:
		for d in xrange(0, D):
			[ in1, in2 ] = tokens.next()
			add_recipe(destruct, in1, in2, True)

	# invocation
	N = int(tokens.next())
	elements = invoke(combos, destruct, tokens.next())
	print('Case #{0}: [{1}]'.format(t + 1, ', '.join(elements)))
