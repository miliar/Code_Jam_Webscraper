#! /usr/bin/env python2.7

T=int(raw_input())

for test in range(1,T+1):
	
	N=int(raw_input())
	Raw_list=raw_input().strip().split()
	Naomi_blocks=[float(weight) for weight in Raw_list]
	Raw_list=raw_input().strip().split()
	Ken_blocks=[float(weight) for weight in Raw_list]
	
	Naomi_blocks.sort()
	Ken_blocks.sort()

	
	#Naomi score in deceitful war
	Ken_blocks_copy=Ken_blocks[:]
	Naomi_blocks_copy=Naomi_blocks[:]
	Naomi_deceitful_score=0
	for i in range(N):
		if (Naomi_blocks_copy[-1]>Ken_blocks_copy[0]): # in this case, Naomi will win, Ken will draw his smallest weight, as he's losing .
			chosen_Naomi=0
			while(Naomi_blocks_copy[chosen_Naomi]<Ken_blocks_copy[0]):
				chosen_Naomi+=1
			# after the loop ends, chosen_Naomi will correspond to the smallest winning block for Naomi
			Naomi_deceitful_score+=1
			Ken_blocks_copy.pop(0)
			Naomi_blocks_copy.pop(chosen_Naomi)
		else :# in this case, Naomi loses, so she will trick Ken in drawing his best block block to win a trifle one 3:)
			Naomi_blocks_copy.pop(0)
			Ken_blocks_copy.pop()
	
	
	#Naomi  score in fair war
	Naomi_fair_score=0
	for i in range(N):
		if (Ken_blocks[-1]>Naomi_blocks[0]): # Ken wins
			chosen_Ken=0
			while(Ken_blocks[chosen_Ken]<Naomi_blocks[0]):
				chosen_Ken+=1
			Ken_blocks.pop(chosen_Ken)
			Naomi_blocks.pop(0)
			
		else :# ken loses
			Ken_blocks.pop(0)
			Naomi_blocks.pop(0)
			Naomi_fair_score+=1
	print "Case #{}: {} {}".format(test, Naomi_deceitful_score, Naomi_fair_score)
	
	