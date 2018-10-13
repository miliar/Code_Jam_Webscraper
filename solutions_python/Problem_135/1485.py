def read_grid(width=4):
	grid = []
	for i in range(width):
		grid.append(list(int(card) for card in raw_input().split(' ')))
	return grid

def outcome(candidates):
	unique_candidates = set(candidates)
	# there are no cards consistent with the volunteer's answers
	if len(unique_candidates) == len(candidates):
		return "Volunteer cheated!"
	# there are multiple cards the volunteer could have chosen
	if len(unique_candidates) < len(candidates) - 1:
		return "Bad magician!"
	# there is a single card the volunteer could have chosen
	for card in unique_candidates:
		candidates.remove(card)
	return candidates[0]

for T in range(int(raw_input())):
	row_num = int(raw_input())
	grid = read_grid()
	candidates = grid[row_num-1]
	
	row_num = int(raw_input())
	grid = read_grid()
	candidates += grid[row_num-1]
	
	print "Case #%d: %s" % (T+1, outcome(candidates))