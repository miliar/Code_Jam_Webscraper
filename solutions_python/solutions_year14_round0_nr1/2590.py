import sets

lines = list(open('A-small-attempt0.in.txt','r'))
output = open('A-small-attempt0.out.txt','w')
attemps = int(lines[0])
for attemp in range (0,attemps):
	index = (attemp * 10) + 1
	a1 = lines[index]
	cards1 = sets.Set(lines[index + int(a1)].split())
	a2 = lines[index + 5]
	cards2 = sets.Set(lines[index + 5 + int(a2)].split())
	sol = cards2.intersection(cards1)
	if (len(sol) == 1):
		output.write("Case #" + str(attemp + 1) + ": " + sol.pop() + "\n")
	elif (len(sol) > 1):
		output.write("Case #" + str(attemp + 1) + ": Bad magician!\n")
	else:
		output.write("Case #" + str(attemp + 1) + ": Volunteer cheated!\n")
