import sys


def play_war(a, b):
	
	naomi_blocks = list(a)
	ken_blocks = list(b)
	
	naomi_points = 0
	ken_points = 0
	
	while len(naomi_blocks) > 0:
		
		naomi_chosen = naomi_blocks.pop(0)
		ken_chosen = -1.0
		for i in range(len(ken_blocks)):
			if ken_blocks[i] > naomi_chosen:
				ken_chosen = ken_blocks[i]
				ken_blocks.remove(ken_chosen)
				break
		if ken_chosen == -1.0:
			ken_chosen = ken_blocks.pop(0)
			
		if naomi_chosen > ken_chosen:
			naomi_points += 1
		else:
			ken_points += 1
		
	return [naomi_points, ken_points]
	

def play_d_war(a, b):

	naomi_blocks = list(a)
	ken_blocks = list(b)
	
	naomi_points = 0
	ken_points = 0
	
	small_margin = 0.0000001
	
	while len(naomi_blocks) > 0:
		
		naomi_chosen = naomi_blocks.pop(0)
		if naomi_chosen > ken_blocks[-1]:
			ken_chosen = ken_blocks.pop(0)
			
		else:
			if naomi_chosen > ken_blocks[0]:
				ken_chosen = ken_blocks.pop(0)
			else:
				ken_chosen = ken_blocks.pop(-1)
				

		if naomi_chosen > ken_chosen:
			naomi_points += 1
		else:
			ken_points += 1
		
	return [naomi_points, ken_points]
	
	

# Read data file into a list
lines = []
with open(sys.argv[1], "r", encoding="utf-8") as data_file:
	for line in data_file:
		lines.append(line.rstrip('\n'))


# Get total number of test cases
test_cases = int(lines[0])
del lines[0]

# Process each test case
for i in range(test_cases):

	del lines[0]
	
	naomi_blocks = [float(x) for x in lines[0].split(" ")]
	naomi_blocks.sort()
	del lines[0]
	
	ken_blocks = [float(x) for x in lines[0].split(" ")]
	ken_blocks.sort()
	del lines[0]
	
	war_result = play_war(naomi_blocks, ken_blocks)
	naomi_score_war = war_result[0]
	
	d_war_result = play_d_war(naomi_blocks, ken_blocks)
	naomi_score_d_war = d_war_result[0]
	
	print("Case #" + str(i+1) + ": " + str(naomi_score_d_war) + " " + str(naomi_score_war))