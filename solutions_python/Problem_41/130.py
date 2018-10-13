#!/usr/bin/python

import itertools

def getNext(k):
	condition = True
	tuplas = []
	firstIndex = len(k) - 2
	lastIndex = firstIndex + 1
	while firstIndex != -1 and k[lastIndex] <= k[firstIndex]:
		if lastIndex == len(k) - 1:
			firstIndex -= 1
			lastIndex = firstIndex
		lastIndex += 1
	
	if firstIndex == -1:
		lista = []
		for c in k:
			lista.append(c)
		lista.sort()
		lista.insert(0, '0')
		i = 1
		while lista[i] == '0':
			i += 1
		x = lista[i]
		lista.remove(x)
		lista.insert(0, x)
		return int(''.join(lista))
	lastIndexMin = firstIndex + 1
	for i in xrange(lastIndexMin, len(k)):
		if k[i] < k[lastIndex] and k[i] > k[firstIndex]:
			lastIndex = i
	lista = []
	for c in k[0:firstIndex]:
		lista.append(c)
	lista.append(k[lastIndex])
	lista2 = []
	for c in k[firstIndex:lastIndex]:
		lista2.append(c)
	for c in k[lastIndex+1:]:
		lista2.append(c)
	lista2.sort()
	lista.extend(lista2)
	return int(''.join(lista))
		
	
if __name__ == '__main__':
	total = int(raw_input())
	for case in xrange(1, total+1):
		nextN = getNext(raw_input())
		print "Case #%d: %d" % (case, nextN)
	
