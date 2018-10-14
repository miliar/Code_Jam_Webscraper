f = file('D-large.in', 'r')
fo = file('D-large.out', 'w')

stdio = False

def get_input():
	if stdio:
		return raw_input()
	return f.readline()
	
def put_input(s):
	if stdio:
		print s
	else:
		fo.write(s)

num_cases = int(get_input())

for case in range(num_cases):
	num_blocks = int(get_input())
	naomi_blocks = sorted([float(item) for item in get_input().split(" ")])
	ken_blocks = sorted([float(item) for item in get_input().split(" ")])

	score_dec_war = 0
	naomi_indexes, ken_indexes = [0, num_blocks-1], [0, num_blocks-1]
	while naomi_indexes[1] >= naomi_indexes[0]:
		if naomi_blocks[naomi_indexes[0]] > ken_blocks[ken_indexes[0]]:
			score_dec_war += 1
			ken_indexes[0] += 1
			naomi_indexes[0] += 1
		else:
			naomi_indexes[0] += 1
			ken_indexes[1] -= 1
	
	naomi_index, ken_index = 0, 0
	while ken_index < num_blocks:
		if naomi_blocks[naomi_index] > ken_blocks[ken_index]:
			ken_index += 1
		else:
			naomi_index += 1
			ken_index += 1
			
	score_war = num_blocks - naomi_index
	put_input("Case #{}: {} {}\n".format(case+1, score_dec_war, score_war))