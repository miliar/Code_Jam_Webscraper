import sys

def keep_typing(combinations, chars_left, right_probabilities):
	avg_keystrokes = 0

	for char_sequence in combinations:
		prob = probability(char_sequence, right_probabilities)

		extra_strokes = 0
		if 'x' in char_sequence:
			extra_strokes = chars_left + 1 + len(char_sequence) + chars_left + 1
		else:
			extra_strokes = chars_left + 1

		avg_keystrokes += extra_strokes * prob

		# print char_sequence, prob, extra_strokes, avg_keystrokes

	return avg_keystrokes

def hit_backspace(combinations, chars_left, right_probabilities, n):
	avg_keystrokes = 0

	for char_sequence in combinations:
		prob = probability(char_sequence, right_probabilities)


		char_sequence_temp = char_sequence[:len(char_sequence) - n]
		chars_left_temp = chars_left + n

		extra_strokes = n
		if 'x' in char_sequence_temp:
			extra_strokes += chars_left_temp + 1 + len(char_sequence_temp) + chars_left_temp + 1
		else:
			extra_strokes += chars_left_temp + 1

		avg_keystrokes += extra_strokes * prob

		# print char_sequence, n, prob, extra_strokes, avg_keystrokes

	return avg_keystrokes

def press_enter(chars_typed, chars_left):
	return 1 + chars_typed + chars_left + 1

def probability(char_sequence, right_probabilities):
	prob = 1
	for i, char in enumerate(char_sequence):
		if char == 'o':
			prob *= right_probabilities[i]
		else:
			prob *= 1-right_probabilities[i]
	return prob


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

	t = int(f.readline())

	for case in range(t):
		A, B = [int(x) for x in f.readline().split()]
		probs = [float(x) for x in f.readline().split()]

		B = B - A

		a = []
		for i in range(A):
			a.append(['o', 'x'])

		b = generate_combinations([], a)

		results = [keep_typing(b, B, probs)]

		for i in range(A):
			results.append(hit_backspace(b, B, probs, i+1))

		results.append(press_enter(A, B))

		print "Case #{}: {:.6f}".format(case+1, min(results))
