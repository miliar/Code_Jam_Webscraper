#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys

def __solveCase(case, fIn, fOut):
	data = fIn.readline().split().__iter__()
	
	combinations = {}
	for i in xrange(int(data.next())):
		tmp = data.next()
		combinations[__sort(tmp[0:2])] = tmp[2]
	
	opposites = {}
	for i in xrange(int(data.next())):
		opposites[__sort(data.next())] = True

	data.next() # elements number, disregard
	elements = data.next()
	# print "combinations:", combinations
	# print "opposites:", opposites
	# print "elements:", elements
	
	list = []
	for element in elements:
		if len(list) == 0:
			list.append(element)
			continue
		
		# find combinations
		pair = __sort(list[-1] + element)
		newElement = combinations.get(pair)
		if newElement:
			
			# found a combination, remove last index
			del list[-1]
		else:
			newElement = element
		
		# find opposites
		oppositeFound = False
		if len(opposites) > 0:
			for element in unique(list):
				pair = __sort(element + newElement)
				if pair in opposites:
					oppositeFound = True
					break
	
		if oppositeFound:
			del list[:]
		else:
			list.append(newElement)
	
	formattedList = __format(list)
	print "Case #{0}: {1}".format(case, formattedList)
	fOut.write("Case #{0}: {1}\n".format(case, formattedList))

def __format(list):
	str = "["
	for i, e in enumerate(list):
		if i > 0:
			str += ", "
		str += e
	str += "]"
	return str

def __sort(pair):
	if pair[0] > pair[1]:
		return pair[1] + pair[0]
	else:
		return pair

def unique(list):
	items = set()
	for item in list:
		if item not in items:
			items.add(item)
			yield item

inName = sys.argv[1]
if inName.find(".in") > -1:
	outName = inName.replace(".in", ".out")
else:
	outName = inName + ".out"

with open(inName) as fIn:
	with open(outName, "w") as fOut:
		cases = int(fIn.readline())
		for i in xrange(1, cases + 1):
			__solveCase(i, fIn, fOut)
