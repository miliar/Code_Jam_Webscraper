#!/usr/bin/python
import sys

finput = sys.argv[1]
fi = open(finput)
num = int(fi.readline())

def divisions(candies, left, right):
	if len(candies) == 1:
		if len(left):  yield [left, right+[candies[0]]]
		if len(right): yield [left+[candies[0]], right]
	else:
		for i in divisions(candies[1:], left+[candies[0]], right):
			yield [i[0], i[1]]
		for i in divisions(candies[1:], left, right+[candies[0]]):
			yield [i[0], i[1]]

	
def patrick(candies):
	if candies == [] : return 0
	return reduce(lambda x,y: x^y, candies)

def process(candies):
	res = 0
	if reduce(lambda x,y: x^y, candies):
		return 'NO'
	for i in divisions(candies,[], []):
		if patrick(i[0]) == patrick(i[1]):
			res = max(res, max(sum(i[0]),sum(i[1])))
	return res

for i in range(num):
	tmp = fi.readline().strip("\n").split()
	tmp = fi.readline().strip("\n").split()
	candies = map(int, tmp)
	res = process(candies)
	print ("Case #%i: %s") % (i+1, res)
