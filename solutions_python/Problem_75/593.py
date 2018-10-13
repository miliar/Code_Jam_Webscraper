#!/usr/bin/python2.6
import re
from itertools import chain

class Element():
	def __init__(self, name):
		self.opposing = set()
		self.combining = {}
		self.name = name
	def addOpposingElement(self, element):
		self.opposing.add(element)
	def addCombiningElement(self, element, result):
		self.combining[element] = result

class ElementList():
	def __init__(self):
		self.lst = []
	def add(self, element):
		for combiningElement, result in element.combining.iteritems():
			if len(self.lst) > 0 and self.lst[-1] == combiningElement:
				self.lst[-1] = result
				return
		for key in element.opposing:
			if key in self.lst:
				self.lst = []
				return
		self.lst.append(element)
	def getList(self):
		out = []
		for element in self.lst:
			out.append(element.name)
		return out

def solve(combinationsCount, combinations, oppositionsCount, oppositions, conjuresCount, conjures):
	
	allElements = dict()
	for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
		allElements[letter] = Element(letter)
	lst = ElementList()
	i = 0
	while i < combinationsCount:
		combination = combinations[i]
		allElements[combination[0]].addCombiningElement(allElements[combination[1]], allElements[combination[2]])
		allElements[combination[1]].addCombiningElement(allElements[combination[0]], allElements[combination[2]])
		i += 1
	i = 0
	while i < oppositionsCount:
		opposition = oppositions[i]
		allElements[opposition[0]].addOpposingElement(allElements[opposition[1]])
		allElements[opposition[1]].addOpposingElement(allElements[opposition[0]])
		i += 1
	i = 0
	while i < conjuresCount:
		lst.add(allElements[conjures[i]])
		i += 1
	return lst.getList()

def flatten(zippedList):
	return [item for pair in zippedList for item in pair]

if __name__ == "__main__":
	lineCount = input()
	i = 0
	outputs = []
	while i < lineCount:
		line = raw_input()
		data = flatten(re.findall("([0-9]+) ([^0-9]*)", line))
		output = solve(int(data[0]), data[1].split(' '), int(data[2]), data[3].split(' '), int(data[4]), data[5])
		outputs.append(output)
		i += 1
	for i, output in enumerate(outputs):
		print "Case #%i: %s" % (i + 1, repr(output).replace("'", ""))
