#!/usr/bin/python

import sys

p_val = set('()')
text = ''
words_list = []
keywords = []

def filter_text(text):
	global p_val

	rval = ''

	for x in text:
		if x in p_val:
			rval += x

	return rval

def predict_size(text):
	rval = 0
	in_p = False

	for i in range(len(text)):
		if text[i] == '(':
			# special case
			if text[i+1] == ')':
				return -1
			in_p = True
			rval += 1
		elif text[i] == ')':
			in_p = False
		elif in_p == False:
			rval += 1

	return rval

def parcours_tree(text, tree, iter):
	global words_list
	global keywords

	found = False
	for w in keywords:
		if w[:iter] == text:
			found = True
			break
	if not found:
		return

	if tree == []:
		words_list.append(text)

	for x in tree:
		for k in x.keys():
			parcours_tree(text+k, x[k], iter+1)

# main function
# write code from here
def process(input, output):
	global text
	global words_list
	global p_val
	global keywords

	init = input.readline().rstrip()
	init = init.split()

	words_lenght = int(init[0])
	words = int(init[1])
	nb = int(init[2])

	keywords = []
	for x in range(words):
		t = input.readline().rstrip()
		# add only right sized words
		if len(t) == words_lenght:
			keywords.append(t)

	# fill p_val
	for w in keywords:
		for x in w:
			p_val.add(x)

	for val in range(1, nb+1):
		tree = None
		words_list = []
		answer = 0

		text = input.readline().rstrip()
		text = filter_text(text)

		def get_possibilities_from_end():
			global text
			rval = ''
			pos = len(text)-1
			if text[pos] == ')':
				# multiple possibilities
				for i in range(pos-1, -1, -1):
					if text[i] != '(':
						rval = text[i] + rval
					else:
						text = text[:i]
						break
			elif text[pos] == '(':
				raise ") before ("
			else:
				rval = text[pos]
				if len(text) >= 1:
					text = text[:pos]
				else:
					text = ''

			return rval

		# we only want to work on text that _can_ be valid
		if predict_size(text) == words_lenght:
			for w_idx in range(words_lenght-1, -1, -1):
				t = []
				r = get_possibilities_from_end()
				s = set()

				# before adding it, check it's needed
				for x in r:
					for w in keywords:
						if w[w_idx] == x:
							s.add(x)
							break

				for x in s:
					d = {}
					d[x] = []
					t.append(d)

				if tree is None:
					tree = t
				else:
					for x in t:
						for k in x.keys():
							x[k] = tree
					tree = t

			parcours_tree('', tree, 0)

			for w in words_list:
				for k in keywords:
					if w == k:
						answer += 1
						break

		output.write('Case #%d: %d\n' %(val, answer))

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print "Need file as argument"
		sys.exit(1)

	input_file = sys.argv[1]

	# open the file
	input_handler = open(input_file, 'r')
	output_handler = open(input_file + '.out', 'w+')

	process(input_handler, output_handler)

	# close files
	input_handler.close()
	output_handler.close()
