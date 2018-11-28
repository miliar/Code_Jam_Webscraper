import sys

def solve(x,r,c):
	if (r*c) % x != 0:  
		return "RICHARD"
	elif x > r and x > c: 
		return "RICHARD"
	elif (r==1 or c==1) and x > 2:
		return "RICHARD"
	elif x == 1:  
		return "GABRIEL"
	elif x == 4:
		if r == 4 and c<=2: 
			return "RICHARD"
		elif c == 4 and r<=2:
			return "RICHARD"
		elif r == 4 and c > 2: 
			return "GABRIEL"
		elif c == 4 and r > 2: 
			return "GABRIEL"
		# only works on small board
	else:   
		return "GABRIEL"


if __name__ == '__main__':

	# print solve(3,3,4)

	if len(sys.argv) >= 2:
		fn = sys.argv[1]
		fo = sys.argv[2]
		# run from CLI, 2nd argument is input filename. 3rd is output filename
		# e.g python ovation.py A-small.in A-small.out 

		solutions = [] 

		with open(fn, 'r') as infile: 
			# with open(fn) recommended b/c it handles file opening and closing
			n_cases = int(infile.readline())
			# read the first line to get number of test cases
			for case in range(n_cases):
				x, r, c  = infile.readline().split()
				# tuple unpacking, modify as needed
				solutions.append(solve(int(x),int(r),int(c)))

				# solve things here, add to array of solutions

		with open(fo, 'w') as outfile:
			# creates a file if none exists
			for n_case, solution in enumerate(solutions):
			# assuming you have an array of solutions with one value each
				outfile.write("Case #" + str(n_case+1) + ": " + str(solution) + "\n")




