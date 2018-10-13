def flip(pancake_orientation, flipper_size):

	count_flips = 0
	num_pancakes = len(pancake_orientation)
	flipper_location = 0

	while '-' in pancake_orientation:

		flipper_location = pancake_orientation.index('-')

		if flipper_location <= num_pancakes - flipper_size:

			for i in range(flipper_location, flipper_location + flipper_size):
				if pancake_orientation[i] == '-':
					pancake_orientation[i] = '+'
				else:
					pancake_orientation[i] = '-'
			
			count_flips += 1

		else:
			return 'IMPOSSIBLE'

	return count_flips

f = open('A-large.in')
g = open('a-large.txt', 'w')

num_test_cases = int(f.readline())

for test_case in range(1, num_test_cases + 1):
	given = f.readline().strip().split()	
	s = list(given[0])
	k = int(given[1])
	answer = flip(s, k)
	# final output
	g.write('Case #' + str(test_case) + ': ' + str(answer) + '\n')

g.close()
f.close()