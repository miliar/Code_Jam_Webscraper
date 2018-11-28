# Google Code Jam 2013 - Qualification Round
import math

_input_file = "C-small-attempt0.in"
_output_file = "C-small-attempt0.out"
_output_file_object = None

_linesPerCase = 1
		
with open(_input_file) as fin, open(_output_file , "w") as _output_file_object:
	lines = fin.read().splitlines()
	numOfCases = int(lines[0])
	for x in range(0,numOfCases):
		_output_file_object.write("Case #{0}: ".format(x+1))
		i=1 + x*_linesPerCase
		(sA,sB) = lines[i].split()
		(A,B) = int(sA),int(sB)
		newA = int(math.ceil(math.sqrt(A)))
		newB = int(math.ceil(math.sqrt(B)))
		count = 0
		origrange = range(A,B+1)
		for cand in range(newA,newB+1):
			scand = str(cand)
			scandr = scand[::-1].lstrip("0")
			if scand == scandr:
					cand_square = cand*cand
					scand_square = str(cand_square)
					scandr_square = scand_square[::-1].lstrip("0")
					if cand_square in origrange and scand_square == scandr_square:
						count += 1						
		_output_file_object.write("{0}\n".format(count))
					
				
