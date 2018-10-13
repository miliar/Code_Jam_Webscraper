#!/usr/bin/env python

import sys

class Person():

	def __init__(self, shyness, clapping=False):
		self.shyness = shyness
		self.clapping = clapping

	def clap(self):
		self.clapping = True

	def __str__(self):
		r = "\nShyness : " + str(self.shyness)
		r += "\nclapping : " + str(self.clapping)
		return r

	def __repr__(self):
		return self.__str__()



in_file=open(sys.argv[1], 'r').readlines()

test_case_nb = in_file[0].strip()

test_cases = []
for t in in_file[1:]:
	t=t.strip().split(' ')
	test_cases.append(t)


invite_list = []

# For each test case
for t_num, t in enumerate(test_cases):

	max_shyness = t[0]
	clapping = 0
	invite = []

	# Creating people list
	p_list = []

	for i,g in enumerate(t[1]):
		tmp_list = []
		for p in range(int(g)):
			tmp_list.append(Person(shyness=i))
		p_list.append(tmp_list)


	for i, g in enumerate(p_list):
		# if current number of people clapping is matching current shyness level
		if len(g) > 0:
			if clapping >= i:
				# Persons with this shyness level can clap
				for p in g:
					p.clap()
				clapping += len(g)
			else:
				# Otherwise, we need to invite other people
				clapping_needed = i-clapping
				for n in range(clapping_needed):
					p = Person(shyness=clapping)
					p.clap()
					invite.append(p)
				clapping += len(invite)
		
				# Now they can clap
				if clapping == i:
					# Persons with this shyness level can clap
					for p in g:
						p.clap()
					clapping += len(g)
			
	invite_list.append(invite)


# Output

out_file=open(sys.argv[1]+"_sol", 'w')
sol=""
for ind, i in enumerate(invite_list):
	
	sol += "Case #" + str(ind+1) + ": " + str(len(i)) + "\n"
out_file.write(sol)

