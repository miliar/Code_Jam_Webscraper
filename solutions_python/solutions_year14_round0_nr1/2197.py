def solve(list, rounds):
	for r in range(rounds):
		row_1 = int(list[r*10][0]) - 1
		row_2 = int(list[r*10+5][0]) -1 
		board_1 = list[r*10+1:r*10+5]
		board_2 = list[r*10+6:r*10+10]
		count = 0
		unions = []
		swaps = []
		for i in xrange(4):
			union =  [x for x in board_1[row_1] if x in board_2[i]]
			unions.append(union)
			swaps.append(len(union))
		if(swaps[row_2] == 1):
			print "Case #" + str(r+1) + ": " + unions[row_2][0]
		elif(swaps[row_2] == 0):
			print "Case #" + str(r+1) + ": Volunteer cheated!"
		else:
			print "Case #" + str(r+1) + ": Bad magician!"
					
data = []
with open('A-small-attempt0.in', 'r') as f:
	lines = f.read().splitlines()
	for l in lines:
		data.append(l.split(' '))
num_rounds = int(data[0][0])
curr_round = 0
data = data[1:]
solve(data, num_rounds)



