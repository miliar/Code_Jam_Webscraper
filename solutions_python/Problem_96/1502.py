import sys

def generate_triplet(score, is_surprising):
	result = [score/3, score/3, score/3]
	if score%3 == 0:
		if is_surprising:
			result[0] = result[0] -1
			result[2] = result[2] +1
	elif score%3 == 1:
		result[2] = result[2] + 1
	else:
		if is_surprising:
			result[2] = result[2] + 2
		else:
			result[1] = result[1] + 1
			result[2] = result[2] + 1
	return result

def find_result(list_of_triplets,p):
	result = 0
	for triplet in list_of_triplets:
		#print triplet
		if max(triplet) >= p:
			result = result + 1
	return result

def can_be_surprising(point):
	return (point >= 3) and (not (point % 3 == 1))

input = open(".\B-small-attempt0.in", "r")
num_of_cases = int(input.readline())
for i in range(1,num_of_cases+1):
	args = input.readline().split()
	num_of_dancers = int(args[0])
	num_of_surprise = int(args[1])
	p = int(args[2])
	total_points = []
	for point in args[3:]:
		total_points.append(int(point))
	total_points.sort(reverse=True)
	triplets = []
	surprisable_points = []
	non_surprisable_points = []
	for point in total_points:
		if can_be_surprising(point):
			surprisable_points.append(point)
		else:
			non_surprisable_points.append(point)

	for j, point in enumerate(surprisable_points):
		if p > (point/3) and num_of_surprise > 0:
			triplets.append(generate_triplet(point, True))
			num_of_surprise = num_of_surprise - 1
			continue
		elif j + num_of_surprise == len(total_points):
			triplets.append(generate_triplet(point, True))
			num_of_surprise = num_of_surprise - 1
			continue
		else:
			triplets.append(generate_triplet(point, False))
			continue
	for point in non_surprisable_points:
		triplets.append(generate_triplet(point, False))
	
	print "Case #%d:" % (i), find_result(triplets, p)
