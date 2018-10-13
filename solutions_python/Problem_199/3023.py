def flip(side):
	if side == "+":
		return  "-"	
	if side == "-":
		return "+"
def stringToList(writing):
	wlist = []
	for i in writing:
		wlist.append(i)
	return wlist
def change(alist,alength,aindex):
	for i in range(alength):
		alist[aindex] = flip(alist[aindex])
		aindex += 1
	return alist		
	
	
		
def happyface(caketext,flipperSize):
	cakelist = stringToList(caketext)
	movenum = 0
	length = len(cakelist)
	for i in range(length):
		if length-i == flipperSize:
			if cakelist[i] =="-":
				movenum = movenum + 1
				cakelist =  change(cakelist,flipperSize,i)			
			for b in cakelist[i:]:
				if b == "-":
					return "IMPOSSIBLE"
			
			else:
				return str(movenum)
		elif cakelist[i] == "-":
			cakelist = change(cakelist,flipperSize,i)
			movenum += 1


tasklist=[]
lines = [line.rstrip('\n') for line in open('q1.inp')]
taskcount=int(lines.pop(0));
for i in range(taskcount):
	state,flipSize=lines.pop(0).split(" ")
	flipSize=int(flipSize)
	res=happyface(state,flipSize)
	print ("Case #"+str(i+1)+": "+res)
			  
