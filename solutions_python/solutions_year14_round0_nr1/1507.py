input = open("1input", "r")
output = open("1output", "w")

def readline():
	return input.readline()

def writeline(string):
	output.write(string + "\n")

def main():

	max = int(readline())
	for i in range(max):
		row1 = int(readline())
		set1 = [readline(), readline(), readline(), readline()]
		set1 = set1[row1 - 1].replace("\n", "").split(" ")

		row2 = int(readline())
		set2 = [readline(), readline(), readline(), readline()]
		set2 = set2[row2 - 1].replace("\n", "").split(" ")

		matches = 0
		match = ""

		for d in range(4):
			if set2[d] in set1:
				matches += 1
				match = set2[d]
				if matches > 1:
					break

		if matches == 0:
			writeline("Case #" + str(i + 1) + ": Volunteer cheated!")
		elif matches == 1:
			writeline("Case #" + str(i + 1) + ": " + str(match))
		else:
			writeline("Case #" + str(i + 1) + ": Bad magician!")

main()