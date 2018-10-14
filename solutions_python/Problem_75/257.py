#! /usr/bin/python

def print_spell(spell):
	return str(spell).replace("'","")

def bothin(element_list,x,y):
	return x in element_list and y in element_list

if __name__ == '__main__':
	import sys
	import pdb
	
	f = open(sys.argv[1], 'r')

	invokable = ('Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F')

	test_cases = int(f.readline())
	for i in range(test_cases):
		
		line = f.readline().split()
		C = int(line[0])
		D = int(line[C+1])
		N = int(line[C+1+D+1])

		# Build the combine dictionary
		if C > 0:
			combine_dict = dict((x[0:2],x[2]) for x in line[1:C+1])
			combine_dict.update( (x[1]+x[0],x[2]) for x in line[1:C+1])
			#print "c--> ", combine_dict
		else:
			combine_dict = {}

		# Build the clear tuples
		if D > 0:
			opposed_list = [(x[0],x[1]) for x in line[1+C+1: -2]]
			#print "o--> ", opposed_list
		else:
			opposed_list = []

		element_list = []
		for c in line[-1]:

			if c in invokable: # Only add invokable elements
				element_list.append(c)

			if len(element_list) >= 2: # Only do stuff if the list is bigger than 2
				last2 = element_list[-2] + element_list[-1]
				
				if last2 in combine_dict: # Combine Dict
					element_list.pop(); element_list.pop() # Remove last two
					element_list.append(combine_dict[last2]) # Add the new element

				else: # Did not combine
					# Check if anything is opposed
					if any([bothin(element_list,x,y)  for (x,y) in opposed_list]):
						del element_list[:] # clear list

		print 'Case #%d: %s' % ((i+1), print_spell(element_list))
	
	f.close()
