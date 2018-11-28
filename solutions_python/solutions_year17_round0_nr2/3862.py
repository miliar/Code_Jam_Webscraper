import sys

def makelist(var):
	charlist = []
	i=0
	while i < len(var):
		charlist.append(var[i])
		i = i+1
	return charlist


def reset(charlist , current):
	charlist[current-1] = str(int(charlist[current-1]) - 1)
	while current < len(charlist):
		charlist[current] = '9'
		current = current+1
	return charlist


def solve(var):
	charlist = makelist (var)
	if len(var) == 1:
		return var
	else:
		current = 1
		compare = 0
		last = compare
		while current < len(var):
			if compare > 0:
				if charlist[compare] != charlist[compare-1]:
					last = compare 
			if charlist[current] < charlist[compare]:
				charlist = reset (charlist , last+1)
				return charlist
			current = current+1
			compare = compare +1
		return charlist


def formatlist(temp):
	if temp[0] == '0':
		temp.pop(0)
	soln = ''
	for i in temp:
		soln = soln+i
	return soln


if __name__ == "__main__":
	inputlist = [line.rstrip('\n') for line in open(str(sys.argv[1]))]
	cases = inputlist[0]
	inputlist.pop(0)
	index = 0
	for i in inputlist:
		tempSoln = solve(i)
		index = index+1
		hs = open ("soln.txt","a")	
		hs.write('Case #'+str(index)+': '+formatlist(tempSoln)+'\n')
		hs.close()
