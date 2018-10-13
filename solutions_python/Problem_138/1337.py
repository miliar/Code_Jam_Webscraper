#!/bin/python

iterations = raw_input() 

def winning_check (blocks_a, blocks_b) :
	win_flag = 1

for iteration in range(int(iterations)) :
	blocks = int(raw_input())

	naomi_blocks = [ float(value) for value in raw_input().split(" ")]
	ken_blocks = [ float(value) for value in raw_input().split(" ")]
	naomi_blocks.sort()
	ken_blocks.sort()
	real_naomi = list(naomi_blocks)
	real_ken = list(ken_blocks)

	#print real_naomi
	#print real_ken
	
	#deceitful war
	# Things you can do to lie
	# 	Lie that a winning block is very high
	#		Force ken to use a low block (but lose)
	#	Lie that a losing block is  second highest
	#		Force ken to use a high block (but lose)
	naomi_score = 0
	while len(naomi_blocks)!= 0:
		if naomi_blocks[0] > ken_blocks[0]:
			naomi_blocks.pop(0)
			ken_blocks.pop(0)
			naomi_score = naomi_score + 1
			continue
		if naomi_blocks[0] > ken_blocks[-1]:
			break
		if naomi_blocks[0] < ken_blocks[0]:
			naomi_blocks.pop(0)
			ken_blocks.pop(-1)
			continue

	naomi_cheat_score = naomi_score + len(naomi_blocks)

	#real war
	real_naomi_score = 0
	while len(real_naomi)!= 0 :
		naomi_turn = real_naomi.pop(-1)
		if ( real_ken[-1] < naomi_turn ) :
			real_ken.pop(0)
			real_naomi_score = real_naomi_score+1
		else :
			real_ken.pop(-1)
		

	
		
	
	print "Case #%s:" % str(int(iteration+1)),
	print naomi_cheat_score, real_naomi_score
