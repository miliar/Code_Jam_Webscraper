def test_line(line):
	played = set(line)
	if "." not in played:
		if len(played)==1 or (len(played) == 2 and "T" in played):
			return line[0] if line[0] != "T" else line[1]
		return " "
	return "."
	

def test_grid(grid):
	is_complete = True
	for i in range(5):
		for rowcol in range(2):
			if i < 4:
				result = test_line([grid[i if rowcol else j][j if rowcol else i] for j in range(4)])
			else:
				result = test_line([grid[j if rowcol else 3-j][j] for j in range(4)])
			if result in "XO":
				return result + " won"
			if result == ".":
				is_complete = False
	return "Draw" if is_complete else "Game has not completed"

if __name__=='__main__':
	import argparse
	parser = argparse.ArgumentParser(description='Determines who wins each game, in a set of games of Tic-Tac-Toe-Tomek')
	parser.add_argument('--verbose', '-v', action='store_true')
	parser.add_argument('infile', type=str, help='in file')
	parser.add_argument('outfile', type=str, nargs="?", help='out file (defaults to infile with extension changed to .out)')
	args = parser.parse_args()

	infile = open(args.infile, "r")
	outfile = open(args.outfile if args.outfile is not None else args.infile.rsplit(".")[0]+".out", "w")
	tests = int(infile.readline())
	for i in range(tests):
		lines = [list(infile.readline().rstrip()) for _ in range(4)]
		s = "Case #%d: %s"%(i+1, test_grid(lines))
		if args.verbose:
			print s
		outfile.write(s + ("\n" if i < tests-1 else ""))
		infile.readline() # empty line
	infile.close()
	outfile.close()
