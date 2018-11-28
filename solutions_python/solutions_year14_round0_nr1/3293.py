import sys

def magic(filename):
	lines = open(filename).read().splitlines()
	f = open('magic.out','w')

	num_cases = int(lines[0])
	current_line = 1
	for i in range(num_cases):
		firstrowpicked = int(lines[current_line])
		firstgroup = str.split(lines[current_line + firstrowpicked], " ")
		current_line = current_line + 5
		secondrowpicked = int(lines[current_line])
		secondgroup = str.split(lines[current_line + secondrowpicked], " ")

		intersect = list(set(firstgroup) & set(secondgroup))

		if len(intersect) > 1:
			f.write("Case #" + str(i+1) + ": Bad magician!\n")
		elif len(intersect) == 1:
			f.write("Case #" + str(i+1) + ": " + intersect[0] + "\n")
		else:
			f.write("Case #" + str(i+1) + ": Volunteer cheated!\n")

		current_line = current_line + 5

	f.close()

def main():
	magic(sys.argv[1])

if __name__ == "__main__":
    main()