
def parsestr(str):
	parselist = [] # holds [char, num of repeats]
	for j in range(len(str)):
		if j == 0:  # first character
			parselist.append([str[0], 1])
		else:  # other characters
			if str[j] == parselist[-1][0]:  # matches last character
				parselist[-1][1] += 1  # increase counter
			else:
				parselist.append([str[j], 1])
	return parselist

def minmove(strlist, checklist):
	# given string list and check list, find minimum number of moves
	moves = 0
	for str in strlist:
		for let in range(len(checklist)):
			average = checklist[let]
			moves += abs(average - str[let][1])
	return moves
			
			
with open("input.in", 'r') as infile:
	cases = int(infile.readline())
	results = [0] * cases  # holds number of moves
	
	for case in range(cases):
		N = int(infile.readline())
		strlist = []  # list of parsed strings
		for i in range(N):
			str = infile.readline().strip()
			strlist.append(parsestr(str))
		
		for str in strlist:
			if len(str) != len(strlist[0]):
				results[case] = "Fegla Won"
				break
		if results[case]:
			continue
			
		# go down column (string) checking each letter
		# find average counter
		checklist = []
		for let in range(len(strlist[0])):
			totoccurance = 0
			letter = strlist[0][let][0]  # first string, let letter, first thing in list
			for str in range(len(strlist)):
				# DEBUG print(strlist[str])
				try:
					if strlist[str][let][0] == letter:  # matches
						totoccurance += strlist[str][let][1]  # counter
					else:  # can't possibly do it
						results[case] = "Fegla Won"
						break
				except:
						results[case] = "Fegla Won"
						break
			if results[case]:  # not 0
				break

			average = int(totoccurance / len(strlist))  # average occurrence for a letter
			checklist.append(average)

			
		if results[case] == 0:  # uninitialized
			results[case] = minmove(strlist, checklist)
						
	# print out case results
	for case in range(cases):
		print("Case #{}: {}".format(case + 1, results[case]))		