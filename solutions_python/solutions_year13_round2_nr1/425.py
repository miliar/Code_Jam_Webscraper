# -*- coding: utf-8 *-*
from ContestSolver import ContestSolver
from math import log


def eatmotes(size, motes, num):
	numeat = 0
	for i in range(num):
		if motes[i] < size:
			size += motes[i]
			numeat += 1
		else:
			break
	motes = [mote for mote in motes[numeat:]]
	return size, motes, num - numeat


def numoperations(size, motes, nummotes):
	if nummotes == 0:
		return 0
	else:
		if size == 1:
			numadd = nummotes
		else:
			numadd = int(log((motes[0] - 1)/(size - 1))/log(2)) + 1

		if numadd >= nummotes:
			return nummotes
		else:
			size = pow(2, numadd) * (size - 1) + 1
			initmotes = nummotes
			size, motes, nummotes = eatmotes(size, motes, nummotes)
			numops = numadd + numoperations(size, motes, nummotes)
			if numops >= initmotes:
				return initmotes
			else:
				return numops


def solver(case):
	#print "newcase"
	size = case[0][0]
	nummotes = case[0][1]
	motes = case[1]
	motes.sort()
	#print size, motes
	size, motes, nummotes = eatmotes(size, motes, nummotes)
	numops = numoperations(size, motes, nummotes)

	#while nummotes > 0:
		#print size, motes
	#	if size == 1:
	#		numadd = nummotes
	#	else:
	#		numadd = int(log((motes[0] - 1)/(size - 1))/log(2)) + 1
#
#		if numadd >= nummotes:
#			numops += nummotes
#			nummotes = 0
#		else:
#			size = pow(2, numadd) * (size - 1) + 1
#			numops += numadd
#			size, motes, nummotes = eatmotes(size, motes, nummotes)

		#newsize = size
		#finished = True
		#for i in range(1, nummotes):
		#	newsize += newsize - 1
		#	if (motes[0] < newsize):
		#		size = newsize + motes[0]
		#		motes = [mote for mote in motes[1:]]
		#		nummotes -= 1
		#		size, motes, nummotes = eatmotes(size, motes, nummotes)
		#		numops += i
		#		finished = False
		#		break
		#if finished:
		#	numops += nummotes
		#	nummotes = 0
	#print numops
	return [numops]

solution = ContestSolver(solver,
	splitlines=True, nosinglelists=False, specifycasesize=False)
#solution.run("A-test", test=True, ints=True)
#solution.run("A-small-attempt1", ints=True)
solution.run("A-large", ints=True, watch=True)
