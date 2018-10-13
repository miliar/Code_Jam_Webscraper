def choose(num_empty, num_people):
	bathroom = [1]
	bathroom.extend([0] * num_empty)
	bathroom.append(1)

	while num_people > 0:

		occupied = [stall for stall, occupancy in enumerate(bathroom)
		if occupancy == 1]

		biggest_space = max([occupied[i+1] - occupied[i] for i in
			range(len(occupied) - 1)])
		for i in range(len(occupied) - 1):
			if occupied[i+1] - occupied[i] == biggest_space:
				left_occ = occupied[i]
				right_occ = occupied[i+1]
				place_here = left_occ + biggest_space // 2
				bathroom[place_here] = 1
				
				if num_people > 1:
					num_people -= 1
				else:
					y = right_occ - place_here - 1
					z = place_here - left_occ - 1
					num_people -= 1
				break
	return str(y) + ' ' + str(z)

# f = open('C-small.txt')
f = open('C-small-1-attempt0.in')
g = open('c.txt', 'w')

num_test_cases = int(f.readline())

for test_case in range(1, num_test_cases + 1):
	given = f.readline().strip().split()	
	n = int(given[0])
	k = int(given[1])
	answer = choose(n, k)
	# final output
	g.write('Case #' + str(test_case) + ': ' + str(answer) + '\n')
g.close()
f.close()