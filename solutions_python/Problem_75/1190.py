class Magicka:
	numTestCases = 0
	caseNum = 0
	nextLine = ""
	combinations = []
	oppositions = []
	elements = []
	f = None
	output = None
	
	def __init__(self):
		self.f = open("B-large.in")
		self.numTestCases = int(self.f.readline()[:-1])
		self.output = open("B.out", 'w')
				
	def next_case(self):
		self.combinations = []
		self.oppositions = []
		self.elements = []
		
		self.caseNum += 1
		self.nextLine = self.f.readline()[:-1].split(" ")
		divider = 1 + int(self.nextLine[0]) # index dividing combinations and oppositions
		for i in range(1,divider): # number of combinations
			self.combinations.append(list(self.nextLine[i]))
		for i in range(divider + 1, len(self.nextLine)-2):
			self.oppositions.append(list(self.nextLine[i]))
		self.elements = list(self.nextLine[-1])
		
	def solve_case(self):	
		if len(self.elements) == 0: return []
		if len(self.elements) == 1: return self.elements
		answer = []
		answer.append(self.elements[0])
		for elem in self.elements[1:]:
			answer.append(elem)
			if len(answer) < 2:
				continue
			combo = self.combine(answer[-1],answer[-2])
			if not combo == None:
				answer[-2] = combo
				temp = answer.pop()
			if self.opposition(answer) == True:
				answer = []
		return answer
				
	def combine(self, elem1, elem2):
		if self.combinations == []:
			return None
		for c in self.combinations:
			if (elem1 == c[0] and elem2 == c[1]) or (elem1 == c[1] and elem2 == c[0]):
				return c[-1]
		return None
		
	def opposition(self, elems):
		if self.oppositions == []:
			return False
		for o in self.oppositions:
			if elems[-1] in o:
				for e in elems[:-1]:
					if e in o and not e == elems[-1]:
						return True
		return False

	def write_answer(self, answer):
		temp = str(answer).split("'")
		answer = ""
		for ch in temp:
			answer+=ch
		if self.caseNum == self.numTestCases:
			self.output.write("Case #%d: %s" % (self.caseNum, answer))
		else:
			self.output.write("Case #%d: %s\n" % (self.caseNum, answer))

	
def main():
	m = Magicka()
	for k in range(m.numTestCases):
		m.next_case()
		answer = m.solve_case()
		m.write_answer(answer)
		print("caseNum: %d" % m.caseNum)
		print("combinations: %r" % m.combinations)
		print("oppositions: %r" % m.oppositions)
		print("elements: %r\n\n" % m.elements)
	m.output.close()
		
if __name__ == "__main__":
	main()