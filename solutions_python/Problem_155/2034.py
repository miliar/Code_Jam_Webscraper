def solve(Smax, histo):
	standing = 0
	friends = 0
	
	for i in range(0, int(Smax)+1):
		if standing < i :
			friends += 1
			standing += 1;
			
		standing += int(histo[i])
	return friends

			
def load(fname):
	with open(fname) as f:
		content = f.readlines()
		return content
	
	
def save(fname, nr, solution):
	f = open(fname, 'a')
	f.write("Case #" + str(nr+1) + ": " + str(solution) + '\n')
	f.close()

	
def main():
	inputFile = 'input.in'
	outputFile = 'output.out';
	
	open(outputFile, 'w+').close()
	
	content = load(inputFile)
	cases = int(content[0])

	for caseNr in range(0, cases):
		data =content[caseNr+1].split()
		solution = solve(data[0], data[1])
		save(outputFile, caseNr, solution)
		
main()
