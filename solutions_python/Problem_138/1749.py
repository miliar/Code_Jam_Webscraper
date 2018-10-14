filename = 'D-large.in'
input = open(filename,'r')

output = open('output.txt','w')
cases = int(input.readline())

def ken_move(naomis_block, ken_blocks):
	#play the smallest ken_blocks value that is greater than naomis_block
	#print("Naomi is playing " + str(naomis_block))
	for block in ken_blocks:
		if float(block) > float(naomis_block):
			#print("Ken's " + str(block) + " beats " + str(naomis_block))
			return ken_blocks.index(block)
	#if none exists, play the smallest ken_blocks value
	#print("Nothing beats it")
	return 0

def war(naomi_blocks, ken_blocks):
	score = 0
	#naomi's score, NOT ken's
	#assume naomi plays her biggest block
	while(len(naomi_blocks) > 0):
		nmove = naomi_blocks.pop()
		kmove = ken_blocks.pop(ken_move(nmove, ken_blocks))
		if (nmove > kmove):
			score += 1

	return score


def deceitful_war(naomi_blocks, ken_blocks):
	map(float, naomi_blocks)
	map(float, ken_blocks)
	score = 0
	#naomi's score, NOT ken's
	while(len(naomi_blocks) > 0):
	#if nsmall < ksmall, claim it is klarge - 0.0001
	#otherwise, if nsmall > ksmall, claim it is klarge + 0.0001
		if naomi_blocks[0] < ken_blocks[0]:
			nmove = naomi_blocks.pop(0)
			nclaim = float(ken_blocks[-1])-0.000001
		else:
			nmove = naomi_blocks.pop(0)
			nclaim = float(ken_blocks[-1])+0.000001
		kmove = ken_blocks.pop(ken_move(nclaim, ken_blocks))
		#print("ken_blocks is " + str(len(ken_blocks)))
		#print("kmove " + str(kmove))
		#print("nclaim " + str(nclaim))
		if (float(nclaim) > float(kmove)):
				score += 1
				#print("+score")
	#print("d war score is " + str(score))
	return score

for testcaseno in range(1,cases+1):
	n = input.readline()

	naomi_blocks = input.readline()[:-1].split(' ')
	map(float, naomi_blocks)
	naomi_blocks.sort()
	#print(naomi_blocks)

	ken_blocks = input.readline()[:-1].split(' ')
	map(float, ken_blocks)
	ken_blocks.sort()
	#print(ken_blocks)

	dresult = deceitful_war(list(naomi_blocks), list(ken_blocks)) #duplicate lists
	nresult = war(naomi_blocks, ken_blocks)
	output.write("Case #" + str(testcaseno) + ": " + str(dresult) + " " + str(nresult) +'\n')

