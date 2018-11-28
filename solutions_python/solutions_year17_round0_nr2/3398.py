import sys
##print sys.argv[1:]
# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

t = int(lines[0])  # read a line with a single integer
##print t

def cascadecheck(numlist, pos):
	digit = len(numlist) - pos
	#print numlist, "pos: ", pos, "digit: ", digit
	if (pos) ==0 :
		return int("".join(map(str,numlist)))
	elif(int(numlist[pos]) >= int(numlist[pos-1]) ):
		return cascadecheck(numlist, pos-1)
	else:
		choplist = numlist[:pos]
		intnum = int("".join(map(str,choplist))) * 10 **(digit) -1
		return cascadecheck(list(str(intnum)), pos-1)





def getTidy(number):
	numlist = list(number)
	intnum = int(number)
	if (intnum < 10):
		return intnum
	else:
		intnum = cascadecheck(numlist, len(numlist)-1)
	return intnum

################# main
f = open(sys.argv[2], 'w')
for index, line in enumerate( lines[1:]) :
	results = getTidy(line.rstrip('\n'))
  	resultsString = "Case #{}: {}".format(index+1, results)
	f.write(resultsString+'\n')
f.close() 
  # check out .format's specification for more formatting options



