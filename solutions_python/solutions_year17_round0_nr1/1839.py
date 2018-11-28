import os
import sys
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
	cakes = list(test[0])
	K = int(test[1])
	#print("K:",K)
	left = 0
	right = len(cakes)-1
	change_count = 0 #If this > S, there is no solution as the pattern has to repeat.
	next_pos = 0
	#print(cakes)
	if check_done(cakes):
		return str(0)

	while change_count <= len(cakes) and left+K <= right+1:
		if cakes[left] == '-':
			flip(cakes,left,left+K)
			change_count +=1
		elif cakes[right] == '-':
			#print(right-K,right)
			flip(cakes,right-K+1,right+1)
			change_count +=1
		else:
			left +=1
			right -=1

		#print(cakes)
		if check_done(cakes):
			return str(change_count)

	return "IMPOSSIBLE"

def flip(pancakes, start, end):
	for idx,c in enumerate(pancakes[start:end]):
		pancakes[start+idx] = flipping[c]

def check_done(pancakes):
	return '-' not in pancakes

#test = ['+','-','-','-','-','-','+','+']
#print(test)
#flip(test,0,5)
#print(test)

if __name__ == '__main__':
	main()


