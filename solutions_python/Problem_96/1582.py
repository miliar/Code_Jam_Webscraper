f_in = open('/home/anirudh/codejam/p2/q2_input', 'r')
f_out = open('/home/anirudh/codejam/p2/q2_output', 'w')

num = int(f_in.readline())
nus=0
for x in range(num):
	line = f_in.readline()
############################################################porb-starts###########################################
	import shlex
	pebbles = shlex.split(line)
	GOOGLERS = pebbles[0]
	SURPISES = pebbles[1]
	BEST = int(pebbles[2])
	Range_list = []
	GOOG_2 = 3+int(GOOGLERS)
	POOL = []
	for tipol in range(3,GOOG_2):  #Each triplets in a line
		TRIPLETS = int(pebbles[tipol])
#		print TRIPLETS
		Split_list = []
		TRIPLETS_begin = (TRIPLETS/3) - 7 
		TRIPLETS_end = TRIPLETS_begin + 14
		Split_list = []
		for numbers in range(TRIPLETS_begin,TRIPLETS_end):
			TX = numbers
			TX_rest = TRIPLETS - TX
			for numbers_2 in range(TRIPLETS_begin,TRIPLETS_end):
				TY = numbers_2
				TY_rest = numbers_2 - TY
				for numbers_3 in range(TRIPLETS_begin,TRIPLETS_end):
					TZ = numbers_3 
					if TX+TY+TZ == TRIPLETS:
						if TX >= (TY-2) and TX <= (TY+2) and TX >= (TZ-2) and TX <= (TZ+2):
							if TY >= (TZ-2) and TY <= (TZ+2) and TY >= (TX-2) and TY <= (TX+2):
								if TZ >= (TY-2) and TZ <= (TY+2) and TZ >= (TX-2) and TZ <= (TX+2):
#									print "(",TX,',',TY,',',TZ,')    best-',BEST
									mumu = sorted([TX,TY,TZ])
									Split_list.append(mumu)
		for element in Split_list:
			if element not in Range_list:
				Range_list.append(element)
		Range_list.sort()
		tempo=[]
		temp2=[]
		for ita in Range_list:
			if ita[0] == ita[1]+2 or ita[0]+2 == ita[1] or ita[0] == ita[2]+2 or ita[2] == ita[0]+2 or ita[1] == ita[2]+2 or ita[2] == ita[1]+2:
				ita.append("*")
				temp2.append(ita)
			else:
				ita.append("-")
				temp2.append(ita)
		Range_list = []
		tempo.append(TRIPLETS)
		tempo.append(temp2)
		POOL.append(tempo)
####################################combi-prob start###################################
	import itertools
	iterable = ""
	ky_combi=[]
	ky2_combi=[]
	ky3_combi=[]
	for s in range(0,len(POOL)):
		iterable += str(s)
		ky_combi.append(s)
	in_combi = itertools.combinations(iterable,int(SURPISES))
	for x in in_combi:
		temp4=[]
		ky2_combi.append(x)
		for element in ky_combi:
			if str(element) not in x:
				temp4.append(element)
		ky3_combi.append(temp4)
#	print ky2_combi
	len5 = len(ky2_combi)
	count_real=0
	for x in range(0,len5):
		count=0
		for items in ky2_combi[x]:
			pre_final = POOL[int(items)][1][0]
#			print POOL[int(items)][0],POOL[int(items)][1][0]
			if int(pre_final[0]) >= 0 and int(pre_final[1]) >= 0 and int(pre_final[2]) >= 0:
				if int(pre_final[0]) >= BEST or int(pre_final[1]) >= BEST or int(pre_final[2]) >= BEST:
					count+=1
		for items in ky3_combi[x]:
			pre_final = POOL[int(items)][1][1]
#			print POOL[int(items)][0],POOL[int(items)][1][1]
			if int(pre_final[0]) >= 0 and int(pre_final[1]) >= 0 and int(pre_final[2]) >= 0:
				if int(pre_final[0]) >= BEST or int(pre_final[1]) >= BEST or int(pre_final[2]) >= BEST:
					count+=1
		if count > count_real:
			count_real =count
#		print count_real,"============Next Combo================================"
	nus+=1
	f_out.write("Case #"+str(nus)+": "+str(count_real))
###################################combi-prob start###################################
#	break
############################################################porb-ends###########################################
	
	f_out.write("\n")
