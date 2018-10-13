import sys

def main():
	std_input = sys.stdin.read().split('\n')

	no_test_cases = int(std_input.pop(0))
	f = open('output.txt', 'w')

	for i in range(no_test_cases):
		first_row = int(std_input.pop(0)) - 1
		first_row_members = std_input[first_row].split()
		std_input = std_input[4:]
		
		second_row = int(std_input.pop(0)) - 1
		second_row_members = std_input[second_row].split()
		std_input = std_input[4:]

		f.write("Case #" + str(i + 1) + ": " + determineResult(first_row_members, second_row_members) + '\n')
	f.close()

def determineResult(firstRowMembers, secondRowMembers):
	output = 0
	for i in range(4):
			for j in range(4):
				if firstRowMembers[i] == secondRowMembers[j]:
					if output != 0:				
						return "Bad magician!"	
					else:
						output = int(firstRowMembers[i])

	if output == 0:
		return "Volunteer cheated!"

	else:
		return str(output)



if __name__ == "__main__":
	main()

