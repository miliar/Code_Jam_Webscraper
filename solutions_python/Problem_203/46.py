

numInputs = int(input())

for i in range(numInputs):
	R, C = [int(num) for num in input().split(" ")]
	print("Case #" + str(i + 1) + ":")
	lastRow = None
	for rowNum in range(R):
		row = input()
		firstInitial = None
		for initial in row:
			if initial == "?":
				continue
			firstInitial = initial
			break
		if firstInitial is None:
			# empty row
			if lastRow is None:
				continue # there have been no non-empty rows beforehand, will deal with later
			print(lastRow) # can literally just repeat the last row and it will still be rectangular
			continue
		outRow = ""
		lastInitial = firstInitial
		for initial in row:
			if initial == "?":
				outRow += lastInitial
			else:
				outRow += initial
				lastInitial = initial
		print(outRow)
		if lastRow is None:
			for i in range(rowNum):
				print(outRow) # fill out any empty rows that occured earlier
		lastRow = outRow