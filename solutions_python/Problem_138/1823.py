def play_honest(blocks_naomi,blocks_ken):
	win_count = 0
	for naomi_block in blocks_naomi:
		ken_choice = -1
		for index,ken_block in enumerate(blocks_ken):
			if ken_block > naomi_block and (ken_block<blocks_ken[ken_choice] or ken_choice == -1):
				ken_choice = index
		if ken_choice!=-1:
			blocks_ken.pop(ken_choice)
		else:
			win_count += 1
	return win_count

def play_dishonest(blocks_naomi,blocks_ken):
	win_count = 0
	blocks_naomi.sort()
	blocks_ken.sort()
	for i in range(len(blocks_ken)-1,-1,-1):
		ken_block = blocks_ken[i]
		if blocks_naomi[-1]>ken_block:
			win_count+=1
			blocks_naomi.pop()
		else:
			blocks_naomi.pop(0)
#	print blocks_naomi
#	print blocks_ken

#	remove_naomi = []
#	for index_naomi,naomi_block in enumerate(blocks_naomi):
#		if naomi_block<blocks_ken[-1]:
#			blocks_ken.pop(0)
#			remove_naomi.append(index_naomi)
#	remove_naomi.sort(reverse=True)
#
#	for index_naomi in remove_naomi:
#		blocks_naomi.pop(index_naomi)
#
#	print blocks_naomi
#	print blocks_ken
#	blocks_naomi.sort(reverse=True)
#	for naomi_block in blocks_naomi:
#		naomi_true = naomi_block
#		if naomi_block > blocks_ken[0]:
#			naomi_false = naomi_true
#		else:
#			naomi_false = blocks_ken[0]-0.000001
#		if naomi_false>blocks_ken[0]:
#			win_count+=1;
#		blocks_ken.pop(0)

	return win_count

with open("input") as f:
	content = f.readlines()

case_count = 0
entry_count = 0
block_count = 0
blocks_ken = None
blocks_naomi = None


for index,line in enumerate(content):
	line = line.strip()
	if index==0:
		entry_count = int(line)
	elif block_count==0:
		block_count = int(line)
	elif blocks_naomi is None:
		blocks_naomi = map(float,line.split(" "))
	elif blocks_ken is None:
		blocks_ken = map(float,line.split(" "))
		case_count += 1
		print "Case #%s: %s %s"%(case_count,play_dishonest(blocks_naomi[:],blocks_ken[:]),play_honest(blocks_naomi[:],blocks_ken[:]))

		block_count=0
		blocks_naomi=blocks_ken=None