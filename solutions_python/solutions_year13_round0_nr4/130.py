#!/usr/bin/python
'''
2013 Qualification round
Problem D. Treasure
T = number of test cases
K = number of keys we start with
N = number of chests to open

State is defined by:
list of current keys held
list of which chests are still to be opened

Let's try caching checked doors
'''
import sys
from pprint import pprint
debug = '-d' in sys.argv
#fh = sys.stdin

fh = open(sys.argv[1])
cases = int(fh.readline())

def addkeys(k, l):
	#if debug:
	#	print 'addkeys(%s, %s)' % (k, l)
	for i in l:
		k[i] += 1
	return k

def delkeys(d, l):
	for i in l:
		d[i] -= 1
	return d

def check(keys, toopen):
	'''
	keys = list of keys we have
	toopen = list of chests still to be opened
	return a (reversed) list of the order to open in
	otherwise return None
	'''
	if debug:
		print 'start check(%s, %s)' % (keys, toopen)
	if not toopen:
		return [] # we've found a solution
	if not keys:
		return # no keys left to use
	if tuple(toopen) in nosol:
		return
	for ii in range(len(toopen)):
		i = toopen[ii]
		if debug:
			print 'trying to open chests[%s]' % i
		key = chests[i][0] # key required to open chests[i]
		if keys[key] == 0:
			continue # we don't have the key
		# we have they key, so try using it to open chests[i]
		keys[key] -= 1
		addkeys(keys, chests[i][1:])
		del toopen[ii]
		result = check(keys, toopen)
		toopen.insert(ii, i)
		delkeys(keys, chests[i][1:])
		keys[key] += 1
		if result != None:
			result.append(i)
			return result
	nosol[tuple(toopen)] = 1

def sufficientkeys():
	keys = [0] * maxkey
	chestkeys = [0] * maxkey
	addkeys(keys, initial_keys)
	for i in chests[1:]:
		addkeys(keys, i[1:])
		chestkeys[i[0]] += 1
	for i in range(maxkey):
		if chestkeys[i] > keys[i]:
			if debug:
				print 'Insufficient key', i
			return False
	return True

for case in range(1, cases+1):
	if debug:
		print
	print 'Case #%i:' % case,
	keycount, chestcount = [ int(i) for i in fh.readline().split() ]
	initial_keys = [ int(i) for i in fh.readline().split() ]
	assert len(initial_keys) == keycount
	chests = ['start'] # ignore zeroth element
	for i in range(chestcount):
		line = [int(i) for i in fh.readline().split() ]
		assert line[1] == len(line) - 2
		del line[1] # number of keys
		# line = [ key_to_open, key1, key2, ...]
		# where key1, key2, ... are the keys in the chest
		chests.append(line)
	if debug:
		print
		print 'Keys:', initial_keys
		print 'Chests:'
		pprint(chests)
	nosol = {}
	maxkey = max([ max(i) for i in chests[1:]]) + 1
	maxkey = max(maxkey, max(initial_keys) + 1)
	if sufficientkeys():
		result = check(addkeys([0]*maxkey, initial_keys), range(1, len(chests)))
	else:
		result = None
	if result == None:
		print 'IMPOSSIBLE'
	else:
		if debug:
			print 'result:', result
		result.reverse()
		for i in result:
			print i,
		print
	sys.stdout.flush()
