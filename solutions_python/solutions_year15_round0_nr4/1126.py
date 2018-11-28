Tc = int(input())

results = ["None"]*Tc

for i in range(Tc):
	values = str(input())
	values = values.split()
	values = [int(a) for a in values]

	chosenOmnino = values[0]
	gridX = values[1]
	gridY = values[2]

	if(((gridX == chosenOmnino and gridX/2 == gridY and gridX != 2)) or ((gridY == chosenOmnino and gridY/2 == gridX and gridY != 2))):
		results[i] = "RICHARD"
		continue
	elif(((gridX == chosenOmnino and gridX/2 == gridY and gridX == 2)) or ((gridY == chosenOmnino and gridY/2 == gridX and gridY == 2))):
		results[i] = "GABRIEL"
		continue
	elif(chosenOmnino == 1):
		results[i] = "GABRIEL"
		continue
	elif(chosenOmnino == gridX == gridY):
		results[i] = "GABRIEL"
		continue
	elif((gridX * gridY) % chosenOmnino != 0):
		results[i] = "RICHARD"
		continue
	elif(((gridX * gridY) % chosenOmnino == 0) and (gridX * gridY > chosenOmnino)):
		results[i] = "GABRIEL"
		continue
	elif(((gridX * gridY) % chosenOmnino == 0) and (gridX * gridY <= chosenOmnino)):
		results[i] = "RICHARD"
		continue

	if((gridX == 1 or gridY == 1) and (chosenOmnino > 2)):
		results[i] = "RICHARD"
		continue
	else:
		results[i] = "GABRIEL"
		continue

for i in range(len(results)):
	print("Case #"+str(i+1)+": "+results[i])