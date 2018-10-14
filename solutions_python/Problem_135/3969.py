def diffgrids(rowa, rowb, grida, gridb):
	counter = 0
	solution = 0
	for card in (grida[rowa]):
		if card in gridb[rowb]:
			for cardb in (gridb[rowb]):
				if cardb == card:
					solution = card
					counter +=1
	if counter == 0:
		return "Volunteer cheated!"
	elif counter == 1:
		return solution
	else:
		return "Bad magician!"
	
def main():
	a = []
	indeces = []
	grids = []
	with open('data.txt') as fp:
		a = fp.read().splitlines()
		
	numcases =  int(a.pop(0))
	tempgrid = []
	
	for ind in range (len(a)):
		if len(a[ind]) < 4:
			indeces.append(int(a[ind]) - 1)
		else:
			tempgrid.append((a[ind]).split())
			if len(tempgrid) == 4:
				grids.append(tempgrid)
				tempgrid = []
	case = 0
	j = 0
	outfile = open('output.txt', 'w')
	while case < (numcases):
		caseline = "Case #{}: {}".format(case + 1, diffgrids(indeces[j], indeces[j + 1], grids[j], grids[j + 1]))
		print>>outfile, caseline
		j += 2
		case +=1
		
main()
