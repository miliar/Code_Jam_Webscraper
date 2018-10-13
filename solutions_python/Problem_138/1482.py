__author__ = 'Llostris'

import copy

input_filename = 'input2.txt'
output_filename = 'output2.txt'

def form_output(testcase, war_score, deceitful_war_score):
	print "Case #%d: %d %d\n" % (testcase, deceitful_war_score, war_score)
	with file(output_filename, 'a') as output:
		output.write("Case #%d: %d %d\n" % (testcase, deceitful_war_score, war_score))

def war(blocks_per_person, naomis_blocks, kens_blocks):
	score_ken = 0
	score_naomi = 0

	for i in range(len(naomis_blocks)):
		j = 0
		while j < len(kens_blocks) and kens_blocks[j] < naomis_blocks[0]:
			j += 1
		if j >= len(kens_blocks):		# ie. if ken doesn't have a heavier block
			kens_blocks.pop(0)			# he plays the lightest block
			score_naomi += 1			# naomi scores a point
		else:
			kens_blocks.pop(j)
			score_ken += 1
		naomis_blocks.pop(0)

	return score_naomi

def deceitful_war(blocks_per_person, naomis_blocks, kens_blocks):
	# find biggest block in ken's blocks
	# suggest you have a little less
	# play your lowest
	score_naomi = 0
	score_ken = 0

	for i in range(len(naomis_blocks)):
		if kens_blocks[0] < naomis_blocks[0]: # she wins at normal war!
			naomis_blocks.pop(0)
			kens_blocks.pop(0)
			score_naomi += 1
		else:
			naomis_blocks.pop(0)
			kens_blocks.pop(len(kens_blocks) - 1)
			score_ken += 1

	return score_naomi


def play_game(testcase, blocks_per_person, naomis_blocks, kens_blocks):
	naomis_blocks.sort()
	kens_blocks.sort()
	print naomis_blocks
	print kens_blocks
	a = war(blocks_per_person, copy.deepcopy(naomis_blocks), copy.deepcopy(kens_blocks))
	b = deceitful_war(blocks_per_person, naomis_blocks, kens_blocks)
	form_output(testcase, a, b)


if __name__ == '__main__' :
	input_file = open(input_filename)
	input_data = input_file.readlines()
	input_file.close()

	testcases = int(input_data.pop(0))

	file(output_filename, 'w+').close()

	for i in range(testcases) :
		blocks_per_player = int(input_data.pop(0))
		naomi = map(float, input_data.pop(0).split())
		ken = map(float, input_data.pop(0).split())
		# print blocks_per_player
		# print naomi
		# print ken
		play_game(i + 1, blocks_per_player, naomi, ken)
