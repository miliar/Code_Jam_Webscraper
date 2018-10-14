import random 

fileIn = open("A-small-attempt0.in", "r")
fileOut = open("output.in", "w")



loop = fileIn.readline().split()
#print loop[0], type(int(loop[0]))

for i in range(0, int(loop[0]) ):


	#First read in both card grids
	row1 = fileIn.readline().split()
	matrix1 = []
	
	for j in range(0, 4):
		vector = fileIn.readline().split()
		for k in range(0, len(vector)):
			vector[k] = int(vector[k])
		matrix1.append(vector)

	row2 = fileIn.readline().split()
	matrix2 = []
	
	for j in range(0, 4):
		vector2 = fileIn.readline().split()
		for k in range(0, len(vector2)):
			vector2[k] = int(vector2[k])
		matrix2.append(vector2)





	#Then take in the lists chosen and assign them to variables
	choice1 = matrix1[ int(row1[0]) - 1 ]
	choice2 = matrix2[ int(row2[0]) - 1 ]


	#Test Magician's trick
	answer = 0
	value = 0
	for j in range(0, len(choice1) ):
		for k in range(0, len(choice2)):
			if( choice1[j] == choice2[k] ):
				answer += 1
				value = choice1[j]


	#print(answer, choice1, choice2, end="\n")
	#print( "end of magic one", end="\n\n")

	if(answer == 0 ):
		fileOut.write( "Case #" + str(i + 1) + ": " + "Volunteer cheated!"  + "\n")
	elif(answer == 1 ):
		fileOut.write( "Case #" + str(i + 1) + ": " + str(value)  + "\n")
	else:
		fileOut.write( "Case #" + str(i + 1) + ": " + "Bad magician!"  + "\n")

fileIn.close()
fileOut.close()
