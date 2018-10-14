import sys

#Print res
def printRes(case, res):
	print("Case #"+ case + ": " + res)

#Do
def runTCase(line, cNum):
	apeople = []
	values = line.split()
	maxShy = values[0]
	inp = values[1]
	count = int(maxShy) + 1
	ini = 2
	speople = inp
	#print("Max shy:" + str(maxShy)  + " people: " + speople)

	for x in range(0,count):
		apeople.append(int(speople[x]))

	invite_people = 0
	count_people = 0
	alen = len(apeople)
	for x in range(0,count):
		#print("[" + str(x) + "] : " + str(apeople[x]))
		if alen == x:
			pass

		if apeople[x] == 0:
			if count_people > 0:
				count_people = count_people - 1
			else:
				invite_people = invite_people + 1
		else:
			count_people = count_people + apeople[x] - 1

	res = cNum - 1
	printRes(str(cNum),str(invite_people))

#Ini Cases
def ini():
	fo = open("A-large.in")
	#tCases = raw_input()
	case_count = 1
	for i,line in enumerate(fo):
		if i == 0:
			firstLine = line
			" ".join(firstLine.split())
			tCases = int(firstLine)
		else:
			if case_count > tCases:
				break
			runTCase(line,case_count)
			case_count = case_count + 1
	fo.close()

#main
if __name__ == '__main__':
    ini()