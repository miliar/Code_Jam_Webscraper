filename = "A-large.in"
def canflip(stack,size, idx):
	howmany = len(stack)
	return idx+size <= howmany	
def flip(stack,size,idx):
	for i in range(idx,idx+size):
		if stack[i] =='+':
			stack[i] = '-'
		else:
			stack[i] = '+'
	return stack		
def solve(stack, size):
	stacklist = list(stack)
	numflips = 0
	for i in range(len(stacklist)):
		if stacklist[i] != '+':
			if canflip(stacklist,size,i):
				flip(stacklist,size,i)
				numflips+=1
			else:
				return "IMPOSSIBLE"
	return numflips

with open(filename) as f:
	lines = f.read().split("\n")
	k = int(lines[0])
itr=1
ofile = open("pancakelarge.txt",'w')
for line in lines[1:-1]:
	data = line.split(' ')
	num = solve(data[0],int(data[1]))
	ofile.write("Case #" + str(itr) +": "+str(num)+"\n")
	itr+=1
ofile.close()
