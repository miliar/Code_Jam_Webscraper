#!/usr/bin/env python
"""
Invoke as:      ./C.py C small 0

Include the C in the arguments because it is just a part of a file name and to
make the arguments compatible with submitting.

Author: Paul Koppen
Website: http://paulkoppen.com/
"""

from heapq import *


# state = (time spent, falling, waterlevel, position, old positions)
#       = (t, f, H, pos, expos)


def hashstate(state):
	count, A, B, total = state
	return tuple(A + B)

def heuristic(state):
	# time taken so far + minimal time to reach exit = optimistic total time
	# for equal estimates, favour non-falling water
	count, A, B, total = state
	typesA             = types(A)
	typesB             = types(B)
	matches            = typesA & typesB
	summedA            = sum(ai for ai,Ai in A if Ai in matches)
	summedB            = sum(bi for bi,Bi in B if Bi in matches)
	summed             = min(summedA, summedB)
	return total - count - summed

def types(A):
	return set(a[1] for a in A)

def discard(A, Bi):
	# discard from A until type A0 == type Bi
	for i,(ai,Ai) in enumerate(A):
		if Ai == Bi:
			return A[i:]

def recurs(count, A, B):
	# harvest
	while A and B and A[0][1] == B[0][1]:
		ai,Ai = A[0]
		bi,Bi = B[0]
		if ai < bi:
			count += ai
			B[0]   = (bi-ai, Bi)
			A      = A[1:]
		elif bi < ai:
			count += bi
			A[0]   = (ai-bi, Ai)
			B      = B[1:]
		else:
			count += ai
			A      = A[1:]
			B      = B[1:]
	# one line empty. end of recursion
	if not A or not B:
		return count
	# pick a new type to match
	typesA = types(A)
	typesB = types(B)
	shared = typesA & typesB
	if not shared:
		return count
	c = max(recurs(count,discard(A,T),discard(B,T)) for T in shared)
	return c

def expand(state):
	count, A, B, total = state
	
	# as long as type A0 == type B0
	#    always consume as far as possible, add to count
	# then either consume from A until type A0 == type B0
	#      or consume from B until type A0 == type B0
	
	empty = False
	ai,Ai = A.pop(0)
	bi,Bi = B.pop(0)
	while Ai == Bi:
		if ai < bi:
			count += ai
			bi    -= ai
			if A:
				ai,Ai  = A.pop(0)
			else:
				return [(count,[],[],total)]
				break
		elif bi < ai:
			count += bi
			ai    -= bi
			if B:
				bi,Bi  = B.pop(0)
			else:
				return [(count,[],[],total)]
				break
		else:
			count += ai
			if A and B:
				ai,Ai  = A.pop(0)
				bi,Bi  = B.pop(0)
			else:
				return [(count,[],[],total)]
				break
	
	# now either dump A or dump B
	A = [(ai,Ai)] + A
	B = [(bi,Bi)] + B
	
	typesA  = types(A)
	typesB  = types(B)
	matches = typesA & typesB
	
	newstates = [(count,discard(A,T),discard(B,T),total) for T in matches]
	
	return newstates


def solve(N, M, A, B):
	""" inputs vary between different challenges, so adapt.
	output must be an iterable of strings, even if the answer is one string
	"""
	return ('%d' % recurs(0,A,B),)
	pool   = []
	hashes = dict()
	total  = min(sum(ai for ai,Ai in A), sum(bi for bi,Bi in B))
	state0 = (0, A, B, total)
	heappush(pool, (heuristic(state0),state0))
	hashes[hashstate(state0)] = heuristic(state0)
	bestsol = 0
	while len(pool):
		heur,state = heappop(pool)
		if len(state[1]) == 0 or len(state[2]) == 0:
			#return ('%d' % state[0],)
			bestsol = max(state[0], bestsol)
			continue
		for newstate in expand(state):
			newhash = hashstate(newstate)
			newheur = heuristic(newstate)
			if newhash in hashes and hashes[newhash] <= newheur:
				continue
			else: hashes[newhash] = newheur
			heappush(pool, (newheur,newstate))
	#return ("0",)
	return (str(bestsol),)


def challenges(T, lines):
	""" yield challenge parameters one set at a time
	there are T challenges
	lines is an iterator over the input file, producing tokenized lines
	"""
	# note this passes each token as a separate argument to solve()
	for i in xrange(T):
		N,M = map(int, lines.next())
		A   = lines.next()
		A   = [(long(A[2*j]),int(A[2*j+1])) for j in xrange(N)]
		B   = lines.next()
		B   = [(long(B[2*j]),int(B[2*j+1])) for j in xrange(M)]
		#if i != 1: continue
		print 'Test case #%d' % (i+1)
		yield (N, M, A, B)



#================================================================= DEFAULT SETUP
def main(fnamein, fnameout, fnamesol=''):
	""" Solve the set of problems defined in a file.
	If solution file exists verify output.
	"""
	
	"""
	Open up the input file and set up a simple line parser
	"""
	# T challenges (test cases), possibly more lines
	fin        = open(fnamein)
	T          = int(fin.next())
	lines      = (l.rstrip('\r\n').split(' ') for l in fin)
	
	"""
	Read and parse the challenges one by one, compute the answer and write to
	file
	"""
	answers    = (solve(*ch) for ch in challenges(T, lines))
	with open(fnameout, 'w') as fout:
		fout.writelines('Case #%d: %s\n' % (i+1, ' '.join(ans))    \
					for i,ans in enumerate(answers))
	fin.close()
	
	"""
	If a solution file exists, verify the produced answer
	"""
	try:
		with open(fnamesol) as fsol:
			sol = fsol.read().rstrip('\r\n')
		with open(fnameout) as fout:
			out = fout.read().rstrip('\r\n')
	except IOError:
		pass
	else:
		if sol == out:
			print 'Correct: Good Job!'
		else:
			print 'Incorrect: Wrong Answer'


if __name__ == '__main__':
	import sys
	params = tuple(sys.argv[1:4])
	fnamein    = '%s-%s-%s.in'  % params
	fnameout   = '%s-%s-%s.out' % params
	fnamesol   = '%s-%s-%s.sol' % params
	main(fnamein, fnameout, fnamesol)
	print 'done.'
