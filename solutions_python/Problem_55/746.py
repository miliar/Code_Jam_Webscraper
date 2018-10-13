#
#  ThemePark.py
#  
#
#  Created by FEI LIU on 5/7/10.
#  Copyright (c) 2010 ucla. All rights reserved.
#

#R --- rTimes
#K --- kPeople
#G --- GList
#N --- nListSize

def themePark(rTimes, kPeople, gList, nListSize):
	if(nListSize <= 0):
		return 0
	if(rTimes <= 0):
		return 0
	if(kPeople <= 0):
		return 0
	
	m = 0
	sum = 0
	overThan = 0
	while(m < nListSize):
		if(gList[m]>kPeople):
			overThan = 1
			return sum
		sum += gList[m]
		m += 1
	
	if(sum <= kPeople):
		return rTimes*sum

	dollar = 0	
	i = 0
	while(rTimes):
	 	#crtP current People
		crtP = 0
		while((crtP + gList[i]) <= kPeople):
			#i = i + 1
			crtP = crtP + gList[i]
			#gList.append(gList.pop(0))	
			i += 1
			if(i >= nListSize):
				i = 0

		dollar = dollar + crtP
		rTimes = rTimes - 1
	
	return dollar
