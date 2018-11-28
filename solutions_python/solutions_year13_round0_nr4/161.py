#!/usr/bin/env python

import sys


def tryopen (closed_chests, available_keys, chestkeys, opening_sequence):
	if 0 == len (closed_chests):
		return opening_sequence

	print >>sys.stderr, "trying... closed: '%s' \nhave keys: %s\nchest keys: %s\nseq: %s" % (closed_chests, available_keys, chestkeys, opening_sequence)

	for n in sorted (closed_chests.keys()):
		need_key = closed_chests[n]
		if need_key in available_keys:
			print >>sys.stderr, "opening chest %s" % n
			new_seq = opening_sequence
			if "" != opening_sequence:
				new_seq += " "
 			new_seq += str (n)

			new_chests = dict (closed_chests)
			del new_chests[n]

			new_keys = dict (available_keys)
			new_keys[need_key] -= 1
			if 0 >= new_keys[need_key]: del new_keys[need_key]

			for m in chestkeys[n]:
				if m in new_keys: new_keys[m] += 1
				else: new_keys[m] = 1

			new_chestkeys = dict (chestkeys)
			del new_chestkeys[n]

			if solvable (new_chestkeys, new_keys, new_chests):
				result = tryopen (new_chests, new_keys, new_chestkeys, new_seq)
				if result: 
					print >>sys.stderr, "SUCCESS!"
					return result
				else: print >>sys.stderr, "BACKTRACKING2\n\n\n"
			else: print >>sys.stderr, "not solvable BACKTRACKING1\n\n\n"



def total_solvable (chestkeys, freekeys, chests):
	solvable = True
	total_keys = {}
	need_keys = {}

	for l in chestkeys.values():
		for k in l:
			if k in total_keys: total_keys[k] += 1
			else: total_keys[k] = 1

	for (k, n) in freekeys.items():
		if k in total_keys: total_keys[k] += n
		else: total_keys[k] = n

	for n in chests.values():
		if n in need_keys: need_keys[n] += 1
		else: need_keys[n] = 1

	for (k, n) in need_keys.items():
		if n > total_keys[k]:
			print >> sys.stderr, "need %d keys of number %d but only %d available" % (n, k, total_keys[k])
			solvable = False
			break
		else: print >>sys.stderr, "need %d keys of number %d, have %d. ok" % (n, k, total_keys[k])

	return solvable



def solvable (chestkeys, freekeys, chests):
	ok = True
	print >>sys.stderr, "free keys: %s, chested keys: %s, chests: %s" % (freekeys, chestkeys, chests)

	for (n, needs_key) in chests.items():
		ok = False
		print >>sys.stderr, "chest %d needs key %d" % (n, needs_key)
		if needs_key in freekeys:
			print >>sys.stderr, "freely available"
			ok = True
			continue

		print >>sys.stderr, "not freely available"
		for (chest, keylist) in chestkeys.items():
			if chest == n: continue
			print >>sys.stderr, "%d has %s" % (chest, keylist)
			if needs_key in keylist:
				print >>sys.stderr, "but in chest %d" % chest
				ok = True
				break

		if not ok: 
			print >>sys.stderr, "NOT OK, chest %d" % n
			break

	return ok



def solve (casenum, chests, startkeys, chestkeys):
	result = ""

	if total_solvable (chestkeys, startkeys, chests): 
		result = tryopen (chests, keys, chestkeys, "")
	else: 
		print >>sys.stderr, "SKIPPED since impossible"

	if not result: result = "IMPOSSIBLE"

	print "Case #%d: %s" % (casenum, result)
	print >>sys.stderr, "Case #%d: %s" % (casenum, result)
	print >>sys.stderr, "===================================="



num_testcases = int (sys.stdin.readline())

for case in range (1, num_testcases+1):
	keys = {}
	chests = {}
	chestkeys = {}

	(numkeys, numchests) = map (int, sys.stdin.readline().split())
	keyarray = map (int, sys.stdin.readline().split())
	print >>sys.stderr, "start keys: ", keyarray
	assert (len (keyarray) == numkeys)
	for n in keyarray:
		if n in keys:
			keys[n] += 1
		else:
			keys[n] = 1

	for n in range (1, numchests+1):
		line = map (int, sys.stdin.readline().split())
		key_needed = line[0]
		chests[n] = key_needed

		num_keys_inside = line[1]
		keys_inside = line[2:]
		
		chestkeys[n] = keys_inside
		print >>sys.stderr, "chest %d has keys: %s" % (n, keys_inside)		

	solve (case, chests, keys, chestkeys)
