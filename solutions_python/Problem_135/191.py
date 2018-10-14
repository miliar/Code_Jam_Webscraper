file = open('input', 'r')

problems = int(file.readline())

for i in range(1, problems+1):
	row = int(file.readline())
	for j in range(0,row-1): 
		x = file.readline() # skip uninteresting lines
	possible = set(file.readline().split())
	for j in range(0,4-row): 
		x = file.readline() # skip uninteresting lines
	row = int(file.readline())
	for j in range(0,row-1): 
		x = file.readline() # skip uninteresting lines
	possible = possible.intersection(file.readline().split())
	for j in range(0,4-row): 
		x = file.readline() # skip uninteresting lines
	if len(possible) == 1:
		print 'Case #' + str(i) + ': ' + possible.pop()
	elif len(possible) <= 0:
		print 'Case #' + str(i) + ': Volunteer cheated!'
	else:
		print 'Case #' + str(i) + ': Bad magician!'

