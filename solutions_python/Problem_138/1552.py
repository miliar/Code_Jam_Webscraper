# -*-coding:Utf-8 -*

import sys

# Parse args
with open("D-large.in") as f:
	arg = f.readlines()

T = int(arg[0])
N = [0 for x in range(T)]
Naomi = [0 for x in range(T)]
Ken = [0 for x in range(T)]
for ct in range(T):
	N[ct] = int(arg[1+ct*3])
	Naomi[ct] = map(float, arg[2+ct*3].split())
	Ken[ct] = map(float, arg[3+ct*3].split())
	
f = open('D-large.out','w')

# Compute each case
for ct in range(T):
	# Print data in memory
	#print "N : " + str(N[ct]) + "\n"
	#print "Naomi: "
	#print Naomi[ct]
	#print "Ken: "
	#print Ken[ct]
	
	KaomiScore = [0 for x in range(2)]
		
	# Both Deceitful War and War need sorted list
	Naomi[ct].sort()
	Ken[ct].sort()
	
	# Kaomi play Deceitful War 
	NaomiDW = list(Naomi[ct])
	KenDW = list(Ken[ct])
	while(len(NaomiDW) > 0):
		if(NaomiDW[0] > KenDW[0]):
			# Kaomi say a number equal to Ken heaviest masse plus epsilon
			# Since Ken play War, he think he can't win this round, so he will use his lightest masse (Ken[0])
			KaomiScore[0] += 1
			NaomiDW.pop(0)
			KenDW.pop(0)
		else:
			# Kaomi can't win, so she say a number equal to Ken heaviest masse minus epsilon
			# She play her lightest masse while Ken will use his best one
			NaomiDW.pop(0)
			KenDW.pop()
			
	# Kaomi play War
	while(len(Naomi[ct]) > 0):
		# Kaomi automatically call her best move each turn
		KaomiMove = Naomi[ct].pop()
		if(KaomiMove < Ken[ct][len(Ken[ct])-1]):
			# Ken can win, so he use his best move 
			Ken[ct].pop()
		else:
			# Ken minimise his damage by using his lightest masse
			KaomiScore[1] += 1
			Ken[ct].pop(0)
	
	# Print output
	f.write ("Case #" + str(ct+1) + ": " + str(KaomiScore[0]) + " " + str(KaomiScore[1]) + "\n")
