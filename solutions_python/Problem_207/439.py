import os
from math import *

T = int(raw_input())

for case in range(0,T):
	N, R, O, Y, G, B, V  = raw_input().split()
	N = int(N)
	R = int(R)
	O = int(O)
	Y = int(Y)
	G = int(G)
	B = int(B)
	V = int(V)
	## So what I think is the crux here is that no one color of hair
	## can be in half the horses. So we can just add together the colors
	## in the "mix breeds" and if it is MORE than half, then we say it's
	## impossible. We do need to find out the distribution though also...
	R_tot = R
	R_tot += O
	R_tot += V
	B_tot = B
	B_tot += G
	B_tot += V
	Y_tot = Y
	Y_tot += O
	Y_tot += G
	
	if  R_tot > N / 2:
		print "Case #" +str(case+1) + ": IMPOSSIBLE"
		continue # move on to next test case
	if  B_tot > N / 2:
		print "Case #" +str(case+1) + ": IMPOSSIBLE"
		continue # move on to next test case
	if  Y_tot > N / 2:
		print "Case #" +str(case+1) + ": IMPOSSIBLE"
		continue # move on to next test case

	#~ print "We have to solve case ", case+1
	
	sol_string = ""
	#~ print "solString is ", sol_string, " N is ", N, "R is ", R, " Y is ", Y, " B is ", B

	## I mean a neater datastructure instead of using N etc would just be 
	## to have a giant tuple with all of the letters maybe
	## I guess we can try just starting to place out the mixed ones. 
	while O > 0:
		O -= 1
		N -= 1
		if sol_string == "" or sol_string[-1] != "B":
			if B < 2:
				print "IMPOSSIBLE because orange"
				continue
			sol_string = "BOB" 
			B -= 2
			N -= 2
		else:
			if B < 1:
				if N == 0: ## We are at the end of the rope...
					sol_string += "O"
					break
			sol_string += "OB"
			B -= 1
			N -= 1
	# We have placed all the orange horses. 

	while V > 0:
		V -= 1
		N -= 1
		if sol_string == "" or sol_string[-1] != "Y":
			if Y < 2:
				print "IMPOSSIBLE because violet"
				continue
			sol_string = "YVY" 
			Y -= 2
			N -= 2
		else:
			if Y < 1:
				if N == 0: ## We are at the end of the rope...
					sol_string += "V"
					break
			sol_string += "VY"
			Y -= 1
			N -= 1
	# We have placed all the violet horses. 

	while G > 0:
		G -= 1
		N -= 1
		if sol_string == "" or sol_string[-1] != "R":
			if R < 2:
				print "IMPOSSIBLE because green"
				continue
			sol_string = "RGR" 
			R -= 2
			N -= 2
		else:
			if R < 1: # We have no more reds to shield the grens. 
				if N == 0: ## We are at the end of the rope...
					sol_string += "G"
					break
			sol_string += "GR"
			R -= 1
			N -= 1
	# We have placed all the green horses. 
	if R > B and R > Y:
		sol_string = "R"
		R -= 1
		N -= 1
	elif B > R and B > Y:
		sol_string = "B"
		B -= 1
		N -= 1
	elif Y > R and Y > B:
		sol_string = "Y"
		Y -= 1
		N -= 1
	elif R > 0:
		sol_string = "R"
		R -= 1
		N -= 1
	elif B > 0:
		sol_string = "B"
		B -= 1
		N -= 1
	elif Y > 0:
		sol_string = "Y"
		Y -= 1
		N -= 1
	else:
		print "WHAT IS GOING ON HERE"
	## I guess if there are any red or green left. 
	while N > 0:
		#~ print "solString is ", sol_string, " N is ", N, "R is ", R, " Y is ", Y, " B is ", B
		## Okay this is perhaps the ugliest thing I have ever done...
		if N == 3 and R == 1 and Y == 1 and B == 1:
			if sol_string[-1] == "R" and sol_string[0] == "R":
				sol_string += "YRB"
				break
			if sol_string[-1] == "R" and sol_string[0] == "Y":
				sol_string += "YRB"
				break
			if sol_string[-1] == "R" and sol_string[0] == "B":
				sol_string += "BRY"
				break
			if sol_string[-1] == "B" and sol_string[0] == "R":
				sol_string += "YRB"
				break
			if sol_string[-1] == "B" and sol_string[0] == "Y":
				sol_string += "YRB"
				break
			if sol_string[-1] == "B" and sol_string[0] == "B":
				sol_string += "RBY"
				break
			if sol_string[-1] == "Y" and sol_string[0] == "R":
				sol_string += "RBY"
				break
			if sol_string[-1] == "Y" and sol_string[0] == "Y":
				sol_string += "RYB"
				break
			if sol_string[-1] == "Y" and sol_string[0] == "B":
				sol_string += "RBY"
				break

		
		if sol_string[-1] == "R":
			if B > Y:
				sol_string += "B"
				B -= 1
				N -= 1
			elif Y > B:
				sol_string += "Y"
				Y -= 1
				N -= 1
			elif sol_string[0] == "Y": ## prioritize to GET THEM OUT NOW. 
				sol_string += "Y"
				Y -= 1
				N -= 1
			else:
				sol_string += "B"
				B -= 1
				N -= 1
		elif sol_string[-1] == "Y":
			if R > B:
				sol_string += "R"
				R -= 1
				N -= 1
			elif B > 0:
				sol_string += "B"
				B -= 1
				N -= 1
			elif sol_string[0] == "R": ## prioritize to GET THEM OUT NOW. 
				sol_string += "R"
				R -= 1
				N -= 1
			else:
				sol_string += "B"
				B -= 1
				N -= 1

		elif sol_string[-1] == "B":
			if Y > R:
				sol_string += "Y"
				Y -= 1
				N -= 1
			elif R > 0:
				sol_string += "R"
				R -= 1
				N -= 1
			elif sol_string[0] == "Y": ## prioritize to GET THEM OUT NOW. 
				sol_string += "Y"
				Y -= 1
				N -= 1
			else:
				sol_string += "R"
				R -= 1
				N -= 1

	print "Case #" +str(case+1) + ": "  + str(sol_string)

	
