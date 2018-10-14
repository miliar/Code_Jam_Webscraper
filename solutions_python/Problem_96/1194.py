def is_surprising(combination):
	if combination[2] - combination[1] == 2 or combination[2] - combination[0] == 2 or combination[1] - combination[0] == 2:
		return True
	return False

input_file_lines = open("B-large.in").readlines()
del input_file_lines[0]

for line_number, line in enumerate(input_file_lines):
	result = "Case #" + str(line_number + 1) + ": "
	scores = line.split()
	del scores[0]
	s = int(scores[0])
	del scores[0]
	p = int(scores[0])
	del scores[0]
	surprising = {}
	normal = {}
	identifier = 1

	for score in scores:
		combinations = []
		for score_a in range(0, 11):
			for score_b in range(0, 11):
				for score_c in range(0, 11):
					if abs(score_c - score_b) <= 2 and abs(score_c - score_a) <= 2 and abs(score_b - score_a) <= 2:
						if score_c + score_b + score_a == int(score):
							combinations.append(sorted([score_c, score_b, score_a]))

		for combination in combinations:
			if max(combination) >= p:	
				if is_surprising(combination):
					if s > 0:
						surprising[score + str(identifier)] = combination
				else:
					normal[score + str(identifier)] = combination

		identifier += 1

	for normal_key in normal.keys():
		if normal_key in surprising:
			del surprising[normal_key]

	if len(surprising) > s:
		print result + str(s + len(normal))
	else:
		print result + str(len(surprising) + len(normal))
