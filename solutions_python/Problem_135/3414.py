'''
Created on Apr 11, 2014

@author: Mike
'''

import pprint

pp = pprint.PrettyPrinter(indent=2)

class TestCase :
	
	def __init__(self) :
		self.grid1 = []
		self.grid2 = []
		pass
	
	def solve(self):
		self.possibleChoices = self.grid1[self.pick1-1]
		self.secondChoices = self.grid2[self.pick2-1]
		self.solutions = list(set(self.possibleChoices).intersection(set(self.secondChoices)))
		return self.solMap(len(self.solutions))
	
	def solMap(self,solutions):
		if(solutions == 0) :
			return "Volunteer cheated!" 
		elif(solutions == 1) :
			return str(self.solutions[0])
		else :
			return "Bad magician!"

def readCases():
	f = open('A-small-attempt0.in', 'r')
	caseCount = int(f.readline())
	cases = []
	for i in range(0,caseCount)  :
		t = TestCase()
		t.pick1 = int(f.readline())
		for i in range(0,4) :
			t.grid1.append([int(x) for x in f.readline().split()])
		t.pick2 = int(f.readline())
		for i in range(0,4) :
			t.grid2.append([int(x) for x in f.readline().split()])
		cases.append(t)
	return cases

""

def main():
	cases = readCases()
	i = 1
	for case in cases :
		print "Case #" + str(i) + ": " + case.solve()
		i += 1
	
	pass

if __name__ == '__main__':
	main()
	pass