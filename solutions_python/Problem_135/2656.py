f = open("aoutput.txt","w")
T = input()
casenum = 1
while casenum<=T:
	gridline1 = []
	gridline2 = []
	answer1 = input()
	for x in range(4):
		if(x==answer1-1): gridline1 = [int(gridnum) for gridnum in raw_input().strip().split()]
		else: raw_input()
	answer2 = input()
	for x in range(4):
		if(x==answer2-1): gridline2 = [int(gridnum) for gridnum in raw_input().strip().split()]
		else: raw_input()
	gridcollab = gridline1+gridline2
	match = []
	for num in set(gridcollab):
		if(gridcollab.count(num) == 2): 
			match.append(num)
	if match:
		if len(match) == 1: f.write("Case #"+str(casenum)+": "+str(match[0])+"\n")
		else: f.write("Case #"+str(casenum)+": Bad magician!\n")
	else: f.write("Case #"+str(casenum)+": Volunteer cheated!\n")
	casenum+=1
f.close()
