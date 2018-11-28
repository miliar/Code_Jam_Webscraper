import sys

#Brandon Shar
#ominos.py
#
#No error handling exists in this program, it must be executed with two command line params
#the first for the file path for input data, the second for output
#and all input is assumed to be valid

#can this number form a pyramid esque shape that changes the parts of the problem
#from even to odd
#other conditions prevent us from having to make this too rigorous
def canPyramid(x, m):
	return (x > 2 and (x%2)==0 and (x/2) == m)


inFile = sys.argv[1]
outFile = sys.argv[2]


file = open(inFile)
output = open(outFile, 'w')

tests = file.readline()

#get test cases
for k in range(int(tests)):
	line = file.readline()
	line = [int(i) for i in line.split()]
	x = line[0]
	r = line[1]
	c = line[2]

	#get our simple cases out of the way

	#1 is a big win
	if(x == 1):
		output.write("Case #" + str(k+1) + ": GABRIEL\n")
		continue

	#any omino bigger than a six can surround a hole
	if(x > 6):
		output.write("Case #" + str(k+1) + ": RICHARD\n")
		continue

	if(x > r * c):
		output.write("Case #" + str(k+1) + ": RICHARD\n")
		continue

	#if our remaining pieces arent divisible
	if(((r * c) % x) != 0):
		output.write("Case #" + str(k+1) + ": RICHARD\n")
		continue

	#ceiling division through opposite floor division
	max_width = -(-x // 2)

	if(x > r and x > c):
		output.write("Case #" + str(k+1) + ": RICHARD\n")
		continue

	if(max_width > r or max_width > c):
		output.write("Case #" + str(k+1) + ": RICHARD\n")
		continue

	#clever trap four block
	if(canPyramid(x,min([r, c]))):
		output.write("Case #" + str(k+1) + ": RICHARD\n")
		continue	


	#none of that stopped him. gooo Gabriel!
	output.write("Case #" + str(k+1) + ": GABRIEL\n")







