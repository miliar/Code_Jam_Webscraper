def is_square(apositiveint):
	if (apositiveint == 1):
		return True, 1
	x = apositiveint // 2
	seen = set([x])
	while x * x != apositiveint:
		x = (x + (apositiveint // x)) // 2
		if x in seen: return False, 0
		seen.add(x)
	return True, x

palindromes = {}
squares = {}
#print palindromes[9]

num_cases = int(raw_input())
for case in range(1,num_cases+1):
	print "Case #"+str(case)+":",
	line = raw_input()
	line = line.split();
	A = int(line[0])
	B = int(line[1])
	count = 0
	for num in range(A,B+1):
		if num not in palindromes:
			numStr = str(num)
			if (numStr == numStr[::-1]):
				palindromes[num] = True
				if num not in squares:
					isSquare, square = is_square(num)
					if (isSquare):
						squares[num] = True, square
						if square not in palindromes:
							squareStr = str(square)
							if (squareStr == squareStr[::-1]):
								palindromes[square] = True
								count+=1
							else:
								palindromes[square] = False
						else:
							if palindromes[square]:
								count+=1
					else:
						squares[num] = False, 0
				else:
					isSquare, square = squares[num]
					if (isSquare):
						if square not in palindromes:
							squareStr = str(square)
							if (squareStr == squareStr[::-1]):
								palindromes[square] = True
								count+=1
							else:
								palindromes[square] = False
						else:
							if palindromes[square]:
								count+=1					
			else:
				palindromes[num] = False
		else:
			if (palindromes[num]):
				if num not in squares:
					isSquare, square = is_square(num)
					if (isSquare):
						squares[num] = True, square
						if square not in palindromes:
							squareStr = str(square)
							if (squareStr == squareStr[::-1]):
								palindromes[square] = True
								count+=1
							else:
								palindromes[square] = False
						else:
							if palindromes[square]:
								count+=1
					else:
						squares[num] = False, 0
				else:
					isSquare, square = squares[num]
					if (isSquare):
						if square not in palindromes:
							squareStr = str(square)
							if (squareStr == squareStr[::-1]):
								palindromes[square] = True
								count+=1
							else:
								palindromes[square] = False
						else:
							if palindromes[square]:
								count+=1					
			
	print count





