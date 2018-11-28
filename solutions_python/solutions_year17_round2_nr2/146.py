#this is a mess...
for L in range(int(input())):
	(_,R,O,Y,G,B,V) = [t(s) for t,s in zip((int,int,int,int,int,int,int),input().split())]
	#O = RY so beside B
	#G = YB so beside R
	#V = BR so beside Y
	
	#four groups: O, G, V, S
	#O is BOBOBO
	#G is RGRGRG
	#V is YVYVYV
	#S is single-colored ones beside each other
	
	bits = { "R": 1, "O": 1|2, "Y": 2, "G": 2|4, "B": 4, "V": 4|1 }
	
	gG = ""
	gV = ""
	gO = ""
	
	while G:
		R -= 1
		G -= 1
		gG += "RG"
	
	while V:
		Y -= 1
		V -= 1
		gV += "YV"
	
	while O:
		B -= 1
		O -= 1
		gO += "BO"
	
	if bool(gO)+bool(gG)+bool(gV)==1 and R==0 and Y==0 and B==0: # just a double-color link is fine
		print("Case #"+str(L+1)+":", gG+gV+gO)
		continue
	
	#can't form double-color links, too few single-color
	if R<0 or Y<0 or B<0:
		print("Case #"+str(L+1)+":", "IMPOSSIBLE")
		continue
	
	#can't append to double-color links so they act like a loose one
	if (gG and not R) or (gV and not Y) or (gO and not B):
		print("Case #"+str(L+1)+":", "IMPOSSIBLE")
		continue
	
	#insufficient horses to link the single-colors
	if R>Y+B or Y>R+B or B>R+Y:
		print("Case #"+str(L+1)+":", "IMPOSSIBLE")
		continue
	
	#if no red, alternate the YB
	if not R:
		if Y != B:
			print("Case #"+str(L+1)+":", "IMPOSSIBLE")
			continue
		out = "YB"*Y
		out = out.replace("Y", gV+"Y", 1)
		out = out.replace("B", gO+"B", 1)
		print("Case #"+str(L+1)+":", out)
		continue
	
	#always put a red one first
	gS = "R"
	R -= 1
	
	while R or Y or B:
		last = gS[-1]
		if last=="R":
			if Y>B:
				gS += "Y"
				Y -= 1
			else:
				gS += "B"
				B -= 1
		if last=="Y":
			if R>=B: # favor R early, so it doesn't end up last
				gS += "R"
				R -= 1
			else:
				gS += "B"
				B -= 1
		if last=="B":
			if R>=Y:
				gS += "R"
				R -= 1
			else:
				gS += "Y"
				Y -= 1
		if R<0 or Y<0 or B<0: 1/0 # assert
	if gS[-1]=="R": 1/0
	
	out = gS
	out = out.replace("R", gG+"R", 1)
	out = out.replace("Y", gV+"Y", 1)
	out = out.replace("B", gO+"B", 1)
	print("Case #"+str(L+1)+":", out)
