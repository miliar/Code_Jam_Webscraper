import sys

AUDIENCE = 1
def parse(filename):
	""" Parse the given file,
		return a list of tuples, each representing a store.
		The first index is the credit in the store and the second
		is a list of prices for the items in the store"""
	operas = []
	
	with open(filename, 'r') as file:
		cases_count = int(file.readline())
		# Read all cases
		for case_line in file:
			audience_raw = case_line.split()[AUDIENCE]
			audience = [int(c) for c in audience_raw]
			operas.append(audience)
			
	return operas
	
def solve(operas):
	solution = [solve_opera(audience) for audience in operas]
	return solution

def solve_opera(audience):
	to_add = 0
	sum_people = 0
	for shyness, count in enumerate(audience):
		if sum_people < shyness:
			to_add += shyness - sum_people
			sum_people = shyness
		sum_people += count
	return to_add
	
FILENAME = 1
def main():
	operas = parse(sys.argv[FILENAME])
	solution = solve(operas)
	for case, sol in enumerate(solution):
		print("Case #%d: %d"%(case+1, sol))
	
if __name__ == "__main__":
    main()