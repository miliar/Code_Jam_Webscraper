

def parseRows(rows):
		thisRow = rows
		thisRow = thisRow.strip().split(' ')

		for j in range(len(thisRow)):
			thisRow[j] = int(thisRow[j], 10)

		return thisRow

def bad(num):
	return "Case #" + str(num+1) + ": Bad magician!"

def cheated(num):
	return "Case #" + str(num+1) + ": Volunteer cheated!"

def good(num, selected):
	return "Case #" + str(num+1) +": " + str(selected)

count = raw_input()

rows = []
selectedRow = []
secondSelectedRow = []
for iteration in range(int(count)):
	selectedRow.append(int(raw_input(),10) - 1)
	row = []

	row.append(raw_input())
	row.append(raw_input())
	row.append(raw_input())
	row.append(raw_input())

	secondSelectedRow.append(int(raw_input(),10) - 1 + 4)
	row.append(raw_input())
	row.append(raw_input())
	row.append(raw_input())
	row.append(raw_input())

	for i in range(len(row)):
		row[i] = parseRows(row[i])
	rows.append(row)

for iteration in range(int(count)):
	error = False
	row = rows[iteration]

	potentialSelectionRow = row[selectedRow[iteration]]
	potentialSelection = set(potentialSelectionRow)

	#check if cheated

	if len(potentialSelection & set(row[secondSelectedRow[iteration]])) == 0:
		string = cheated(iteration)
		error = True

	#we good
	if (not error):
		if len(list(potentialSelection & set(row[secondSelectedRow[iteration]]))) == 1:
			singleElement = list(potentialSelection & set(row[secondSelectedRow[iteration]]))[0]
			string = good(iteration, singleElement)
		else:
			string = bad(iteration)

	print(string)
