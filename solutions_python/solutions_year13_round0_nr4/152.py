#!/usr/bin/env python

import sys
import operator
from math import sqrt, floor, ceil
from collections import Counter

class InputFile:
	def __init__(self, fd):
		self.fd = fd
	def readInt(self):
		return int(self.fd.readline())
	def readIntegers(self):
		return tuple([int(x) for x in self.fd.readline().split()])
	def readIntegersList(self):
		return [int(x) for x in self.fd.readline().split()]
	def readString(self):
		return self.fd.readline()[:-1]


def solve(stato, casse, mancanti, fatte, level=0):
	#print "-> ", stato, casse, mancanti, fatte
	#print fatte
	
	if len(mancanti) == 0:
		return fatte
	
	iter_mancanti = list(mancanti)
	
	# Euristica
	if True:
		bilancio = Counter()
		bilancio.update(stato)
		
		for ch in iter_mancanti:
			bilancio.update(casse[ch]['cont'])
		
		# che sia possibile pagare ogni cosa
		for ch in iter_mancanti:
			bilancio.subtract(casse[ch]['cont'])
			if bilancio[casse[ch]['req']] <= 0:
				return None
			bilancio.update(casse[ch]['cont'])

		# che il bilancio sia positivo
		bilancio.subtract([casse[ch]['req'] for ch in iter_mancanti])
		if bilancio.most_common()[-1][1] < 0:
			return None
		
	
	# Backtrack ordinato
	iter_mancanti.sort()
	for ch in iter_mancanti:
		if stato[casse[ch]['req']] > 0:
			if ch not in mancanti:
				print "ERRORE-3"
				sys.exit(1)
			
			stato.subtract([casse[ch]['req']]) # paga
			stato.update(casse[ch]['cont'])  # saccheggia
			mancanti.remove(ch)              # togli da mancanti
			fatte.append(ch)                 # aggiungi a fatti
			
			result = solve(stato, casse, mancanti, fatte, level+1)
			if result is not None:
				return result
			
			fatte.pop()                      # togli da fatti
			mancanti.add(ch)                 # aggiungi a mancanti
			stato.subtract(casse[ch]['cont'])  # restituisci
			stato.update([casse[ch]['req']])   # riprenditi il pagamento
			
	return None

inputfile = InputFile(sys.stdin)
T = inputfile.readInt()
for case in range(1,T+1):
	(k, n) = inputfile.readIntegers()
	#print k, n
	
	keys = inputfile.readIntegersList()
	if len(keys) != k:
		print "ERROR-1", keys, k
		sys.exit(1)
	
	casse = []
	mancanti = set()
	for ch in range(n):
		a = inputfile.readIntegersList()
		if len(a) < 2 or len(a)-2 != a[1]:
			print "ERROR-2"
			sys.exit(1)
		req = a[0]
		cont = a[2:]
		casse.append(dict(req = req, cont = cont))
		mancanti.add(ch)
	
	stato = Counter(keys)
	result = solve(stato, casse, mancanti, [])
	
	if result is None or len(result) < n: 
		print "Case #%d: IMPOSSIBLE" % case
	else:
		print "Case #%d: %s" % (case, " ".join([str(x+1) for x in result]))

