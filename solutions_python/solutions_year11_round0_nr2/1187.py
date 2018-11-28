import sys,os

class NonBaseElement:
	def __init__(self, str):
		self.a, self.b, self.replacement = [ x for x in str ]
		
	def replace(self, output):
		for i in range(2): output.pop()
		output.append(self.replacement)
		return output

	def matches(self, output):
		if len(output) >= 2:
			cmpa,cmpb = (output[-1], output[-2])
			if (cmpa == self.a and cmpb == self.b) or (cmpa == self.b and cmpb == self.a): return True

class OpposedElement:
	def __init__(self, str):
		self.a, self.b = [ x for x in str ]

	def matches(self, output):
		if output and len(output):
			last = output[-1]
			other = None
			if last == self.a: other = self.b
			if last == self.b: other = self.a
			if other and other in output: return True

sys.stdin.readline()

for case,line in enumerate(sys.stdin):
	parts = line.strip().split(" ")
	parts.reverse()
	C = int(parts.pop())
	nb = []
	for i in range(C):
		nb.append(NonBaseElement(parts.pop()))
	D = int(parts.pop())
	op = []
	for i in range(D):
		op.append(OpposedElement(parts.pop()))
	in_len = parts.pop()
	intput = parts.pop()
	output = []
	for c in intput:
		output.append(c)
		for x in nb:
			if x.matches(output): output = x.replace(output)
		for x in op:
			if x.matches(output): output = []
	
	print "Case #%d: [%s]" % (case+1, ", ".join(output))
	