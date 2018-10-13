
import os, sys, re, string

def readint():
	return int(sys.stdin.readline())
def readints(sp=" "):
	return map(lambda x: int(x), sys.stdin.readline().split(sp))

class Node:
	def __init__(self, value):
		self.value = value
		self.name = None
		self.first = None
		self.second = None

	def output(self):
		print self.name, self.value
		if self.first:
			self.first.output()
			self.second.output()

def compile2tree(code):
	def parse_real(index):
		s = ''
		while code[index] == ' ': index += 1
		while code[index] != ' ' and code[index] != ')':
			s += code[index]
			index += 1
		return index, float(s)

	def parse_alpha(index):
		start = index
		while code[index] != ' ' and code[index] != '(':
			index += 1
		return index, code[start:index]
			
	def parse(index, node):
		while True:
			ch = code[index]
			if ch == ')':
				return index, node
			if ch == '(':
				index, value = parse_real(index + 1)
				node.value = value
				while True:
					ch = code[index]
					if ch == ')':
						return index, node
					elif ch != ' ':
						index, name = parse_alpha(index)
						node.name = name
						index, child1 = parse(index, Node(1))
						index, child2 = parse(index+1, Node(1))
						node.first = child1
						node.second = child2
						index += 1
					else:
						index += 1
			else:
				index += 1
	return parse(0, Node(1.0))[1]

def compile_animal(text):
	values = text.split(" ")
	res = {}
	for v in values[2:]:
		res[v] = 1
	return res

def calculate(tree, animals):
	def f(node, p):
		if node.name:
			if animals.has_key(node.name):
				return  f(node.first, p*node.value)
			else:
				return  f(node.second, p*node.value)
		else:
			return p*node.value
	return "%1.7f" % f(tree, 1.0)

def operate():
	code = "".join([sys.stdin.readline().strip() for i in range(readint())])
	animals = [compile_animal(sys.stdin.readline().strip()) for i in range(readint())]
	tree = compile2tree(code)
	return "\n".join(map(lambda x: calculate(tree, x), animals))

def main():
	print "\n".join(map(lambda x: "Case #%d:\n%s" % (x, operate()), range(1, readint()+1)))

if __name__ == '__main__':
	main()

