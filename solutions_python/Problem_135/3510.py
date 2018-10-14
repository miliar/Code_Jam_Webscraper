import sys

inp = open(sys.argv[1])

cases = int(inp.readline())

for i in range(0, cases):
	row = int(inp.readline())
	data = ""
	for j in range(0, 4):
		row_data = inp.readline()
		if j+1 == row:
			data = row_data.rstrip().split(" ")
	row2 = int(inp.readline())	
	data2 = ""
	for j in range(0, 4):
		row_data = inp.readline()
		if j+1 == row2:
			data2 = row_data.rstrip().split(" ")

	result = "Volunteer cheated!"
	for j in data:
		for k in data2:
			if j == k:
				if result == "Volunteer cheated!":
					result = j
				else:
					result = "Bad magician!"

	print("Case #" + str(i+1) + ": " + result)
