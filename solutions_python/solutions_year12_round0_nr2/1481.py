import sys
import itertools

def possible_triplets(s):
	triplets = []

	for x in range(11):
		for y in [a for a in range(x-2, x+3) if a >= 0 and a <= 10]: 
			for z in [a for a in range(y-2, y+3) if a in range(x-2, x+3) and a >= 0 and a <= 10 and x+y+a == s]:
				triplet = tuple(sorted( (x, y, z) ))
				if triplet not in triplets:
					triplets.append(triplet)

	return triplets

def is_surprising(triplet):
	return (abs(triplet[0]-triplet[1]) > 1) or (abs(triplet[0]-triplet[2]) > 1) or (abs(triplet[1]-triplet[2]) > 1)

def count_surprising(triplets):
	count = 0
	for triplet in triplets:
		if is_surprising(triplet):
			count += 1

	return count

def generate_combinations(list_combinations, list_triplets):
	if len(list_triplets) == 0:
		return list_combinations
	else:
		if len(list_combinations) == 0:
			return generate_combinations([[x] for x in list_triplets[0]], list_triplets[1:])
		else:
			combinations = []
			for combination in list_combinations:
				for triplet in list_triplets[0]:
					combinations.append(combination + [triplet])
			return generate_combinations(combinations, list_triplets[1:])




if __name__ == '__main__':
	f = open(sys.argv[1])

	t = f.readline()

	i = 1
	for line in f.readlines():
		n, s, p = [int(x) for x in line.split()[:3]]
		sums = [int(x) for x in line.split()[3:]]

		possible_triplets_list = []
		for score_sum in sums:
			possible_triplets_list.append(possible_triplets(score_sum))

		max_p = 0
		for triplet_combination in generate_combinations([], possible_triplets_list):
			if count_surprising(triplet_combination) == s:
				count_scores = 0
				for triplet in triplet_combination:
					for score in triplet:
						if score >= p:
							count_scores += 1
							break
				if count_scores > max_p:
					max_p = count_scores

		print "Case #{}: {}".format(i, max_p)
		i += 1











