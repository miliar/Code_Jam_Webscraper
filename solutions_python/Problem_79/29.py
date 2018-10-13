import sys

input_stream = sys.stdin
output_stream = sys.stdout

t = int(input_stream.readline().strip())

for i in range(t):
	values = input_stream.readline().split()
	n = int(values[0])
	m = int(values[1])

	words = []
	for j in range(n):
		words.append(input_stream.readline().strip())

	output_stream.write("Case #" + str(i + 1) + ": ")

	for j in range(m):
		sequence = input_stream.readline().strip()
		best_value = -1
		best_index = 0
		for k in range(n):
			target_word = words[k]
			letters_tried = set()
			sequence_index = -1
			score = 0

			candidates = n
			while candidates > 1:
				candidates = 0
				unknown_letters = set()
				for p in range(n):
					if (len(target_word) != len(words[p])):
						continue
					diff_letters = set()
					q = 0
					while (q < len(target_word)):
						if (target_word[q] == words[p][q]):
							q += 1
							continue
						if ((target_word[q] in letters_tried) or (words[p][q] in letters_tried)):
							break

						diff_letters.add(target_word[q])
						diff_letters.add(words[p][q])
						q += 1

					if (q == len(target_word)):
						candidates += 1
						unknown_letters = unknown_letters.union(diff_letters)

				if candidates > 1:
					sequence_index += 1
					letters_tried.add(sequence[sequence_index])
					if ((sequence[sequence_index] in unknown_letters) and (target_word.find(sequence[sequence_index]) == -1)):
						score += 1

			if best_value < score:
				best_value = score
				best_index = k

		output_stream.write(" " + words[best_index])

	output_stream.write("\n")


input_stream.close()
output_stream.close()
