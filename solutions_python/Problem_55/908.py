file = open('C-small-attempt2.in')
file.seek(0)
input = file.readlines()
NumberCases = int(input[0][:-1])
input = input[1:]
CaseIndex = 1
while(CaseIndex <= NumberCases):
	CaseSpecs = input[0:2]
	CaseVars = CaseSpecs[0][:-1].split(" ")
	Groups = CaseSpecs[1][:-1].split(" ")
	Runs = int(CaseVars[0])
	CanHold = int(CaseVars[1])
	NumberGroups = int(CaseVars[2])
	RunIndex = 1
	TotalProfit = 0
	while(RunIndex <= Runs):
		GroupIndex = 0
		PPL = 0
		while(GroupIndex < NumberGroups):
			PPL = PPL + int(Groups[GroupIndex])
			if(PPL > CanHold):
				if(GroupIndex>0):temp = Groups[:GroupIndex]
				elif(GroupIndex==0):temp = Groups[0]
				TotalProfit = TotalProfit + PPL - int(Groups[GroupIndex])	
				Groups = Groups[GroupIndex:] + temp
				break
			if(GroupIndex+1==NumberGroups):
				TotalProfit = TotalProfit + PPL
				break
			GroupIndex = GroupIndex+1
		RunIndex = RunIndex+1
	print "Case #",CaseIndex,":",TotalProfit
	input = input[2:]	
	CaseIndex = CaseIndex+1
						
					
					
					
	
	
	
	
