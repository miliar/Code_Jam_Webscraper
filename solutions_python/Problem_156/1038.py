def houseOfPancakes(D, P, case_num):
	maxMin = 0
	currMin = 0
	print int(8**0.5)
	for Pi in P:
		# print Pi
		currMin = 0
		while Pi > 0:
			if Pi == 1 or Pi == 2:
				currMin += 1
				Pi -= 1
			else:
				if Pi % 2 == 0:	
					amount = Pi**0.5
					Pi -= amount
					distr = True
				else:
					Pi -= 1
				currMin += 1
			# distr = False
		if currMin > maxMin:
			maxMin = currMin
			
	return "Case #{}: {}".format(case_num, maxMin)

if __name__ == '__main__':
	case_num = 1
	#inp = raw_input("Enter: ").split("\n")
	f = open('input10', 'r')
	for i, line in enumerate(f.read().split("\n")):
		if not line: continue
		if i == 0: # T
			continue
		elif i % 2 == 1: # first line of each case
			D = int(line) # int
		elif i % 2 == 0: # second line of each case
			P = [int(x) for x in line.split(" ")] # array of ints
			print houseOfPancakes(D, P, case_num)
			case_num += 1
	f.close()