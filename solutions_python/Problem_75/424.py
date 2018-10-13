filename = "B-large"

f = open("%s.in"  %filename)
o = open("%s.out" %filename, 'w')


class Elements:
	def __init__(self):
		self.combined = []
		self.opposed = []
		self.elements = []

	def feed(self, element):
		self.elements.append(element)
		
		# Combine the last elements
		last = self.elements[-2:]
		for c in self.combined:
			l = [c[0], c[1]]
			if l == last or l[::-1] == last:
				self.elements.pop()
				self.elements[-1] = c[2]

		# Check if there's opposed elements in the list
		for i in self.opposed:
			if i[0] in self.elements and i[1] in self.elements:
				self.elements = []




cases = int(f.readline())

for case in range(cases):
	line = f.readline().split(' ')

	elems = Elements()

	numCombined = int(line.pop(0))
	for i in range(numCombined):
		elems.combined.append(tuple(list(line.pop(0))))

	numOpposed = int(line.pop(0))
	for i in range(numOpposed):
		elems.opposed.append(tuple(list(line.pop(0))))

	for c in line[-1][:-1]:
		elems.feed(c)

	o.write("Case #%d: [%s]\n" %(case + 1, ', '.join(elems.elements)))
	

o.close()
f.close()