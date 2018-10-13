import fileinput
import sys
import math

def isSolvable(armin, enemies):
	katamariSize=armin
	for enemy in enemies:
		if katamariSize > enemy:
			katamariSize += enemy
		else:
			return False
	return True

def numOperationsNeeded(armin, enemies):
	katamariSize = armin
	remaining = len(enemies) + 1
	operations = 0;
	for enemy in enemies:
		remaining -= 1
		if katamariSize > enemy:
			katamariSize += enemy
		else:
			ops = 0
			while katamariSize <= enemy:
				ops += 1
				if katamariSize - 1 > 0:
					katamariSize += katamariSize - 1
				else:
					break
			if ops >= remaining:
				operations += remaining
				return operations
			else:
				operations += ops
				if katamariSize > enemy:
					katamariSize += enemy


	return operations

infile=fileinput.input()
numCases=int(infile.readline())

for case in range(1,numCases+1):
	sys.stdout.write("Case #"+str(case)+": ")

	line1 = infile.readline().strip().split()
	line2 = infile.readline().strip().split()

	armin=int(line1[0])
	numEnemies=int(line1[1])
	enemies=[int(x) for x in line2]
	enemies.sort()



	print(numOperationsNeeded(armin, enemies))

