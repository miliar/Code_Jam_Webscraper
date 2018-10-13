import re

inp = open("in.txt")
out = open("out.txt","w+")


def solve():
	cases = int(inp.readline())
	for case in xrange(cases):
		
		cols = {}
		diag1 = ""
		diag2 = ""
		empty_found = False
		case_lines = 5
		case_won = False
		
		for i in xrange(4):
			row = inp.readline()[:-1]
			case_lines -= 1
			print "row:", row
			won_row = check_won_row(row)
			if won_row:
				write_case(case + 1, won_row, "won")
				case_won = True
				break
			if "." in row:
				empty_found = True
			
			diag1_cell = row[i]
			diag2_cell = row[3 - i]
			if diag1_cell != diag1:
				if diag1 == "":
					diag1 = diag1_cell
					diag2 = diag2_cell
				elif diag1 == "T":
					diag1 = diag1_cell
				elif diag1_cell == "T":
					if i == 3 and diag1 != ".":
						write_case(case + 1, diag1, "won")
						case_won = True
						break
				else:
					diag1 = False
			else:
				if i == 3 and diag1 != ".":
					case_won = True
					write_case(case + 1, diag1, "won")
					break
			
			if diag2_cell != diag2:
				if diag2 == "T":
					diag2 = diag2_cell
				elif diag2_cell == "T":
					if i == 3 and diag2 != ".":
						write_case(case + 1, diag2, "won")
						case_won = True
						break
				else:
					diag2 = False
			else:
				if i== 3 and diag2 != ".":
					write_case(case + 1, diag2, "won")
					case_won = True
					break
					
			
			won = False
			for j in xrange(4):
				col = row[j]
				if i < 3:
					if j not in cols:
						cols[j] = col
					if cols[j] != col:
						if cols[j] == "T":
							cols[j] = col
						elif col == "T":
							pass
						else:
							cols[j] = False
					
				else:
					if col != ".":
						if col == cols[j] or col == "T":
							won = cols[j]
							break
			
			if won:
				write_case(case + 1, won, "won")
				case_won = True
				break
		
		if not case_won:
			if empty_found:
				write_case(case + 1,"Game has not completed")
			else:
				write_case(case + 1, "Draw")
		for i in xrange(case_lines):
			inp.readline()

def check_won_row(row):
	if row in ["XXXX", "TXXX", "XTXX", "XXTX", "XXXT"]:
		return "X"
	if row in ["OOOO", "TOOO", "OTOO", "OOTO", "OOOT"]:
		return "O"
	return None

def write_case(case, *args):
	out.write("Case #%s: %s\n" % (case, " ".join(args)))
	
solve()