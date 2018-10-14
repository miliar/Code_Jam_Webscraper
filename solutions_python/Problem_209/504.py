import copy
import os
from math import *



def PutPancakes(selected_pancake, pancake_list, K):
	total_area = selected_pancake[0] * selected_pancake[0]; # the surface area
	total_area += selected_pancake[0] * selected_pancake[1] * 2
	# now we creat eht list of pancakes as before with the surface area.
	# but now we limit them to the ones that actually fit on top of our
	# pancake. 
	pancakes = []
	for i in range(len(pancake_list)):
		if pancake_list[i][0] > selected_pancake[0]:
			#~ print pancake_list[i], " has bigger radius than ", selected_pancake
			continue # we cannot add this pancake
		area = pancake_list[i][0] * pancake_list[i][1] * 2
		pancakes.append([area, pancake_list[i][0], pancake_list[i][1]])
	if len(pancakes) < K: # WE have too few pancakes 
		return -1
	pancakes.sort()
	#~ print "Before splicing pancakes are " ,pancakes
	for i in range(0, len(pancakes) - (K)):
		pancakes.pop(0)
	#~ pancakes = pancakes[-(K+1):-1]
	#~ print "the pancakes we are adding are", pancakes
	for pancake in pancakes:
		total_area += pancake[2] * pancake[1] * 2
		#~ print "adding ", pancake[2] * pancake[1] * 2

	return total_area
T = int(raw_input())

for case in range(0,T):
	N, K  = raw_input().split()
	K = int(K)
	N = int(N)
	
	## OKAY SO THE EQuation we have is R^2 + R*H. 
	## I guess what we could do is try starting with all pancakes, and then after that selectign 
	## the reminaing K by the simle height criteria.
	pancakes = []
	## We need to pick out the cylinder with the largest area and use 
	## as many of those as possible. a
	for pancake in range(0, N):
		radius, height = raw_input().split()
		radius = int(radius)
		height = int(height)
		pancakes.append([radius, height])
	
	### Okay so now for each possible pancake, we try starting with that. 
	bestArea = -1
	for i in range(0,len(pancakes)):
		newpancakes = copy.deepcopy(pancakes)
		selected = newpancakes.pop(i)
		area = PutPancakes(selected, newpancakes, K-1)
		#~ print "attempting to start iwth", selected, " gives area", area
		if area > bestArea:
			bestArea = area
	#~ print "best area is", bestArea
		#~ pancakes.append([(radius*height * 2), radius, height])
	
	# if K > 2 then we just want to pick teh pancake with the largest radius 
	# only once. 
	#~ print "panckes are", pancakes
	#~ pancakes.sort()
	#~ print "After sorting pancakes are", pancakes
	#~ selected = []
	#~ if K == 1:
		#~ largestArea = -1
		#~ largestIndex = -1
		#~ for i in range(0,N):
			#~ area = (pancakes[i][1] * pancakes[i][1]) + ( pancakes[i][1] * pancakes[i][2] * 2)
			#~ if area > largestArea:
				#~ largestArea = area
				#~ largestIndex = i
		#~ print "pancake with largest area was ", i
		#~ selected.append(pancakes.pop(i))
		#~ K -= 1

	#~ else:
		#~ largestRadius = -1
		#~ largestIndex = -1
		#~ for i in range(0,N):
			#~ if pancakes[i][1] > largestRadius:
				#~ largestRadius = pancakes[1]
				#~ largestIndex = i
		#~ print "pancake with largest radius was ", i
		#~ selected.append(pancakes.pop(i))
		#~ K -= 1
	
	## And now we pick teh K pancakes wiht largest side area
	#~ for pancake in range(0, K):
		#~ selected.append(pancakes.pop())
	
	
	#~ print "the selected pancakes are ", selected

	#~ largestRadius = -1
	#~ largestIndex = -1
	#~ for i in range(0,K):
		#~ if selected[i][1] > largestRadius:
			#~ largestRadius = selected[i][1]
			#~ largestIndex = i
	#~ print "pancake with largest radius was ", largestIndex

	## and now we just compute the area
	#~ area = (selected[largestIndex][1]**2)
	#~ print "surface area upward is " , area
	#~ for pancake in selected:
		#~ print "this pancake is ", pancake
		#~ area += pancake[2] * pancake[1] * 2
		#~ print "adding side area", pancake[2] * pancake[1] * 2
			
	
	print "Case #" +str(case+1) + ": "  + str(bestArea * pi)

 
 
