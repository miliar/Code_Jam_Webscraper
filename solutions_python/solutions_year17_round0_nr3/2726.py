import sys

def solve(ip):
	stall = ip[0]
	peeps = int(ip[1])
	parts = []
	parts.append(int(stall))
	i=0
	y = 0
	z = 0
	while i < peeps:
		largest = max(parts)
		index = parts.index(largest)
		parts.pop(index)
		if largest%2 == 0:
			y = (largest/2)-1
			z = y+1
		else:
			y = largest/2
			z = y
		parts.append(y)
		parts.append(z)
		i = i+1
	return [max([y,z]),min([y,z])]

if __name__ == "__main__":
	inputlist = [line.rstrip('\n') for line in open(str(sys.argv[1]))]
	cases = inputlist[0]
	inputlist.pop(0)
	index = 1
	for line in inputlist:
		soln = solve(line.split(' '))
		hs = open("soln.txt","a")
		hs.write('Case #'+str(index)+': '+str(soln[0])+' '+str(soln[1])+'\n')
		index = index+1
