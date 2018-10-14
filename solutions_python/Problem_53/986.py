#
#  SnapperChain.py
#  
#
#  Created by FEI LIU on 5/8/10.
#  Copyright (c) 2010 ucla. All rights reserved.
#

def snapperChain(nSnappers, kTimes):
	if(kTimes <= 0):
		return 0
	if(nSnappers <= 0):
		return 0

	#remember check nSnappers = 1, 2, 3, 4
	#and kTimes = 1, 2, 3, 4
	
	# initilize two Lists for info
	m = nSnappers
	snList = [] #snapper list
	poList = [] #power list
	while(m>0):
		snList.append(0)
		poList.append(0)	
		m = m -1
	poList[0] = 1
	
	snapperCount = 0
	k = kTimes
	while(k):
		# update the snapper List after each snapped
		i = 0
		firstZero = 0
		while(i < nSnappers):
			if(snList[i] != poList[i]):
				snList[i] = 1
				if(firstZero == 0):
					poList[i] = 1
				else:
					poList[i] = 0
			else:
				snList[i] = 0
				if(firstZero == 0):
					firstZero = 1
					poList[i] = 1
				else:
					poList[i] = 0
			i = i + 1
		snapperCount += 1	
		if(poList[nSnappers-1] == 1 and snList[nSnappers-1] == 1):
			print str(snapperCount)
			break
		# update the Power List after each snapped
		#j = 0
		#firstZero = 0
		#while(j < nSnappers):
		#	if((snList[j] == 1) and (firstZero == 0)):
		#		poList[j] = 1
		#		j += 1
		#		continue
		#	if(snList[j] == 0 and firstZero == 0 ):
		#		poList[j] = 1
		#		firstZero = 1
		#		j += 1
		#		continue
		#	if(firstZero == 1):
		#		poList[j] = 0
		#		j += 1
		#		continue 
		k -= 1
	
	if(poList[nSnappers-1] == 1 and snList[nSnappers-1] == 1):
		if(k != 0):
			if((kTimes-snapperCount)%(snapperCount+1) == 0):
				return 1
			else:
				return 0
		else:
			return 1
	else:
		return 0


