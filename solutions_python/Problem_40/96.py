#!/usr/bin/python

import sys

class Animal:
	def __init__(self):
		self.features = []
		self.name = ""
		self.cool = 1.0

def create_node(lines):
	node = Node()
	read = 1

	i=0
	while lines[i].split() == []:
		i += 1
		read += 1

	l = lines[i].split()

	node.value = float(l[0])

	if (len(l) == 2):
		node.cond = filter_string(l[1])
		node.if_ok, read2 = create_node(lines[read:])
		read += read2
		node.if_not_ok, read2 = create_node(lines[read:])
		read += read2

	return node, read

class Node:
	def __init__(self):
		self.value = 0.0
		self.cond = ""
		self.if_ok = None
		self.if_not_ok = None

def filter_string(s):
	rval = ""
	for x in s:
		if x != '(' and x != ')':
			rval += x
	
	return rval

# main function
# write code from here
def process(input, output):
	nb = int(input.readline().rstrip())

	for val in range(1, nb+1):

		nb_lines = int(input.readline().rstrip())
		lines = []
		for x in range(nb_lines):
			lines.append(filter_string(input.readline().rstrip()))

		root_node, _ = create_node(lines)

		nb_an = int(input.readline().rstrip())
		animals = []
		for x in range(nb_an):
			a = input.readline().rstrip()
			a = a.split()
			animal = Animal()
			for y in range(len(a)):
				if y == 1:
					continue
				if y == 0:
					animal.name = a[y]
				else:
					animal.features.append(a[y])
			animals.append(animal)
		
		output.write('Case #%d:\n' % val)

		# find coolness
		for a in animals:
			node = root_node
			while node is not None:
				a.cool *= node.value
				if node.cond in a.features:
					node = node.if_ok
				else:
					node = node.if_not_ok
			output.write("%.7f\n" % a.cool)

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
