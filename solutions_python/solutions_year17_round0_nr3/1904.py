import os
import sys
import bisect

current = os.getcwd()
outer = os.path.dirname(os.getcwd())
sys.path.append(current)
sys.path.append(outer)

from utils.io import *

flipping = {'-':'+', '+':'-'}

def main():
	start = time_in_ms()
	info = parse_data()
	raw_tests = info[0]
	output_file = info[1]
	results = []

	for idx, r_test in enumerate(raw_tests):
		print("Trying #"+str(idx))
		test = r_test
		results.append(solve(test))
		print(results[-1])

	##print(results)
	data_output(results, output_file)
	print("Time taken:",str(time_in_ms() - start)+"ms")

def solve(test):
	N=int(test[0])
	K=int(test[1])
	stalls = ['_']*(N+2)
	stalls[0] = stalls[-1] = 'X'
	#print(stalls)
	result = None
	occupancy = [0,len(stalls)-1]

	for i in range(1,K+1):
		#print("Placing #:",i)
		result = place_next_person(stalls, occupancy)
		#print(stalls)

	return(str(max(result[:-1]))+" "+str(min(result[:-1])))

def place_next_person(stalls, occupancy):
	l_best = r_best = 0
	idx_best = len(stalls)-1
	occu_idx = 0

	for idx,s in enumerate(stalls):
		if s != '_':
			occu_idx += 1
			continue

		if idx > occupancy[occu_idx]:
			occu_idx += 1


		#l = idx - closest_left(stalls, idx) - 1
		#r = closest_right(stalls, idx) - idx - 1
		l = idx-occupancy[occu_idx-1] - 1
		r = occupancy[occu_idx] - 1 - idx
		#print("idx:",idx,occu_idx,r,l_best,r_best,occupancy[occu_idx-1],occupancy[occu_idx])
		#print(type(r))
		#print(type(r_best))
		#print(min(l,r),min(l_best,r_best))
		if min(l,r)>min(l_best,r_best):
			l_best = l
			r_best = r
			idx_best = idx
		elif min(l,r)==min(l_best,r_best):
			if max(l,r)>max(l_best,r_best):
				l_best = l
				r_best = r
				idx_best = idx
			elif max(l,r)==max(l_best,r_best) and idx<idx_best:
				l_best = l
				r_best = r
				idx_best = idx

		#print(l,r,l_best,r_best, idx_best)


	if stalls[idx_best] != '_':
		print("Stalls are full!")
		return

	stalls[idx_best] = 'P'
	#print("placed @",idx_best,"L_s:",l_best,"R_s:",r_best)
	bisect.insort(occupancy,idx_best)
	#print(occupancy)
	return(l_best,r_best,idx_best)

def closest_left(stalls, pos):
	for idx,s in reversed(list(enumerate(stalls[:pos]))):
		if s != '_':
			return idx
	return "BROOOOOKEN"

def closest_right(stalls, pos):
	for idx,s in enumerate(stalls[pos:]):
		if s != '_':
			return idx+pos
	return "BROOOOOKEN"

if __name__ == '__main__':
	main()


