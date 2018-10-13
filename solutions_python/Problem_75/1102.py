#!/usr/bin/env python

import sys, os

def main(*args):

	#~ I open the input file
	if len(sys.argv) > 1: 
		in_f = open(sys.argv[1], 'r')
	else: 
		in_f = open('_B.in', 'r')

	#~ I get the number of test cases and the input for each test case
	nbr_cases	= int(in_f.readline().strip())
	cases 		= [line.strip().split(" ") for line in in_f]
	in_f.close()

	#~ For each test case...
	for i in range(nbr_cases):
		case = cases[i]
		combinations = dict()
		oppositions	 = dict()

		nbr_combinations = int(case.pop(0))
		for _ in range(nbr_combinations):
			e1,e2,e3 = case.pop(0)
			combinations[(e1,e2)] = e3
			combinations[(e2,e1)] = e3
			
		nbr_oppositions	= int(cases[i].pop(0))
		for _ in range(nbr_oppositions):
			pair = case.pop(0)
			oppositions[pair[0]] = pair[1]
			oppositions[pair[1]] = pair[0]
			
		nbr_base_elements 	= int(case.pop(0))
		base_elements 		= map(str,case.pop(0))
		non_base_elements	= []


		while base_elements != []:
			invoked_element = base_elements.pop(0)

			if non_base_elements == []:
				non_base_elements.append(invoked_element)

			else:
				last_element	= non_base_elements[-1]
				comb			= (last_element,invoked_element)
				if combinations.keys() != [] and comb in combinations.keys():
					non_base_elements.pop()
					base_elements.insert(0,combinations[comb])
				elif oppositions.keys() != [] and invoked_element in oppositions.keys() and oppositions[invoked_element] in non_base_elements:
					non_base_elements = []
				else:
					non_base_elements.append(invoked_element)

		#~ I write down the answer in the output file
		res = "[" + ", ".join(["%s"%(c) for c in non_base_elements]) + "]"
		print "Case #%d: "%(i+1), res
	return 0


#this calls the 'main' function when this script is executed
if __name__ == '__main__': main(sys.argv)
