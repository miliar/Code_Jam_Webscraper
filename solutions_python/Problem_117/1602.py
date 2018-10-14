
def IsValid( lawn, x, y ):
	validX = True
	validY = True
	for i in range(0,len(lawn[0])):
		if lawn[x][i] > lawn[x][y]:
			validX = False
	for j in range(0,len(lawn)):
		if lawn[j][y] > lawn[x][y]:
			validY = False
	return validX or validY

cases = int(raw_input())

lawns = []

for i in range(0,cases):
	lawns.append([])
	dim = raw_input().split(' ')
	x,y = int(dim[0]),int(dim[1])
	for j in range(0,x):
		lawns[i].append([])
		inputstr = raw_input().split(' ')
		for k in range(0,y):
			lawns[i][j].append(inputstr[k])

for i in range(0,len(lawns)):
	valid = True
	for j in range(0,len(lawns[i])):
		for k in range(0,len(lawns[i][j])):
			if not IsValid(lawns[i],j,k):
				valid = False
	
	if valid:
		print "Case #{}: YES".format(i+1)
	else:
		print "Case #{}: NO".format(i+1)


