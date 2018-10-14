#!/usr/bin/env python

def find_triplet(total_score):
	triplet = [10, 10, 10] # The score triplet

	while True:
		triplet_sum = sum(triplet)

		if triplet_sum > total_score:
			# Must lower one of the scores, find the right one
			index_to_lower = -1

			for x in range(3):
				base_score = triplet[x]

				okay_count = 0 # If this count reaches 2, we can subtract 1 from triplet[x]

				for y in range(3):
					if x is y: continue # Skip if we're analysing the same score
					
					other_score = triplet[y]

					score_distance = abs(base_score - other_score)

					if score_distance <= 1:
						if (other_score - base_score) >= -1 and (other_score - base_score) <= 0:
							if base_score > 0:
								# We can subtract 1 from base_score
								okay_count += 1

				if okay_count is 2: # We can subtract 1 from triplet[x] safely
					index_to_lower = x
					break;

			if index_to_lower is -1:
				raise Exception("We're stuck, captain! %d : %s"%(total_score, triplet))
			else:
				triplet[index_to_lower] -= 1

		else:
			return triplet # Houston, we have a triplet

def is_surprising(triplet):
	for x in range(3):
		for y in range(3):
			if x is y: continue
			distance = abs(triplet[x] - triplet[y])
			if distance is 2:
				return True
			elif distance > 2:
				return None
	return False

def best_result(triplet):
	return max(triplet)

def make_surprising(triplet):
	if is_surprising(triplet):
		return triplet

	work_triplet = list(triplet) # Making a copy of triplet

	work_triplet.sort()

	sub_index = -1

	has_added = False

	for n in range(3):
		if sub_index == -1:
			if work_triplet[n] > 0:
				sub_index = n
				work_triplet[n] -= 1
			else:
				continue
		else:
			if n is not sub_index:
				if work_triplet[n] < 10:
					work_triplet[n] += 1
					has_added = True
					break
				else:
					continue

	if not has_added:
		return triplet # Return the triplet as how it was before

	if is_surprising(work_triplet) == None:
		work_triplet[0] += 1
		work_triplet[2] -= 1

	return work_triplet

def triplets_above_threshold(triplets, threshold):
	count = 0
	for triplet in triplets:
		if best_result(triplet) >= threshold:
			count += 1
	return count

def count_surprising(triplets):
	count = 0
	for triplet in triplets:
		if is_surprising(triplet):
			count += 1
	return count

def max_distance(triplet):
	distance = 0
	for x in range(3):
		for y in range(3):
			if x is y: continue
			if abs(triplet[x] - triplet[y]) > distance:
				distance = abs(triplet[x] - triplet[y])
	return distance


# The program itself
def program():
	import sys

	if len(sys.argv) >= 2:
		filename = sys.argv[1]
	else:
		print "No filename specified"
		exit()

	input_file = open(filename)
	input_lines = input_file.readlines()

	lines_count = int(input_lines.pop(0))

	for n in range(lines_count):
		current_line = input_lines[n].split(" ")

		googlers_count = int(current_line.pop(0))
		surprising_count = int(current_line.pop(0))
		minimum_result = int(current_line.pop(0))

		surprising_countdown = surprising_count # Countdown used to make all surprising triplets

		resulting_triplets = list()

		for g in range(googlers_count):
			current_score = int(current_line[g])
			current_triplet = find_triplet(current_score)

			# If we're close to a good result, use up a surprising-triplet-point(TM)
			if (best_result(current_triplet) is minimum_result - 1) and (surprising_countdown > 0):
				new_triplet = make_surprising(current_triplet)
				if is_surprising(new_triplet):
					surprising_countdown -= 1
					current_triplet = new_triplet

			resulting_triplets.append(current_triplet)

		if surprising_countdown > 0: # If we're left with some surprising-triplet-points(TM), let's use them
			for t in range(len(resulting_triplets)):
				if (not is_surprising(resulting_triplets[t])) and surprising_countdown > 0:
					new_triplet = make_surprising(resulting_triplets[t])
					if is_surprising(new_triplet):
						surprising_countdown -= 1
						resulting_triplets[t] = new_triplet

		print "Case #%d: %s"%(n + 1, triplets_above_threshold(resulting_triplets, minimum_result))


	exit()

if __name__ == "__main__":
	program() # Run

	#test4()
