import numpy as np


def googleCodeReporter(testFileName):
	inputFileName = testFileName
	outputFileName = inputFileName[:-3] + ".out"
	print (outputFileName)

	listOut = []
	with open(inputFileName) as inputFile:
		inputFile = list(inputFile)
		sampleSize = int(inputFile[0])
		sampleIndex = range(1,sampleSize+1)

		for x in sampleIndex:
			inputFile[x] = inputFile[x].rstrip()
			print (inputFile[x], type(inputFile[x]))
			value = wide_spatula(inputFile[x])
			listOut.append(''.join(["Case #",str(x),": ", str(value)]))



	with open(outputFileName, 'w') as outputFile:
		for item in listOut:
			outputFile.write("%s\n" % item)





def wide_spatula(case):
	case = case.split(' ')
	
	pancake_string =case[0]
	width = int(case[1])

	flip_count = 0
	pancake_bool = [True if x is '+' else False for x in pancake_string]
	
	pancake_array = np.array(pancake_bool, dtype=bool)
	print ("Original Pancake Ordering :: {}".format(pancake_array))

	# possible = True
	max_flips = pancake_array.size

	while max_flips > 0:
		start_index = 0	
		if pancake_array.all():
			max_flips = 0

		for x_index in range(0,len(pancake_array)):
			# print (x_index)
			if pancake_array[x_index]:
				start_index = x_index

			else:
				try:
					for y in range(x_index, (x_index + width)):
						pancake_array[y] = not pancake_array[y]


					flip_count += 1
					max_flips -= 1

					print ("New Pancake Ordering {}    :: {}".format(flip_count, pancake_array))
				except:
					max_flips = 0
					flip_count = "IMPOSSIBLE"




	if not pancake_array.all():
		flip_count = "IMPOSSIBLE"

	return flip_count


					

googleCodeReporter(testFileName = "A-large.in")