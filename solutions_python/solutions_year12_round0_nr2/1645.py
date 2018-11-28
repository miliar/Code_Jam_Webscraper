#!/usr/bin/env python

#open input file
f = open("B-large.in", "r")

#reading the total number of cases
number = f.readline()

#prepare variables for storing
n_dancers = 0 # number of Googlers dancing N
n_triplets = 0 # number of surprising n_triplets S
boundary_s = 0 # boundary score p
string = [] #input line splitted by spaces; 
case = 0 # number of cases processed

for line in f:
	string = line.split(" ")
	length = len(string)
	total_score = [] # vector for all total score entries
	mod_check = [] # helper vector containing all entries whose average < p
	surprise_check = []
	n_higher = 0 # number of triplets having a higher score than p
	surprise_scores = 0 # number of surprising scores making the cut

	#save fix values
	n_dancers = int(string[0])
	n_triplets = int(string[1])
	boundary_s = int(string[2])

	#save all total score values
	for i in range(3,length):
		total_score.append(int(string[i]))

	#check whether all values of the triplet > p
	for j in range(0, len(total_score)):
		if total_score[j]/3 >= boundary_s:
			n_higher = n_higher + 1
		else:
			mod_check.append(total_score[j])

	if len(mod_check) != 0:
		for h in range(0, len(mod_check)):
			if mod_check[h]%3 == 1:
				if (mod_check[h]/3)+1 >= boundary_s:
					n_higher = n_higher +1
			elif mod_check[h]%3 == 2:
				if (mod_check[h]/3)+1 >= boundary_s:
					n_higher = n_higher +1
				else:
					surprise_check.append(mod_check[h])
			else:
				surprise_check.append(mod_check[h])

		if n_triplets != 0 and len(surprise_check) != 0:
			for k in range(0, len(surprise_check)):
				if surprise_check[k]%3 == 0:
					if (surprise_check[k]/3)+1 >= boundary_s and surprise_check[k] != 0:
						n_higher = n_higher + 1
						surprise_scores = surprise_scores + 1
						if surprise_scores == n_triplets:
							break
				else:
					if (surprise_check[k]/3)+2 >= boundary_s and surprise_check[k] != 0:
						n_higher = n_higher +1
						surprise_scores = surprise_scores + 1
						if surprise_scores == n_triplets:
							break
				
	case = case + 1

	print "Case #"+str(case)+":", str(n_higher)


f.closed