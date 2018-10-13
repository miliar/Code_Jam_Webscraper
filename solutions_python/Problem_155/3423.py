import fileinput
import sys

myfile = fileinput.input();
maxcases = 0
currentcase = 0

for line in myfile:

	if fileinput.isfirstline():
		maxcases = int(line.strip())
		continue

	sections = line.strip().split()
	maxshy = int(sections[0])
	audience = sections[1]

	currentcase += 1;
	sys.stdout.write("Case #"+str(currentcase)+": ")	
	sys.stdout.flush()

	clappingnow = 0
	needtoinvite = 0
	for currentshy in range(maxshy+1):
		if (int(audience[currentshy]) and (currentshy > clappingnow)):
			needtoinvite += currentshy - clappingnow
			clappingnow += needtoinvite
		clappingnow += int(audience[currentshy])

	print needtoinvite

	if maxcases == currentcase:
		break
