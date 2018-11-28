i = 0
num_iter = 0
lines = []
out = open('output.txt', 'w')

with open('A-large.in') as f:
	lines = f.readlines()
	num_iter = int(lines[0])
	i+=1

while i <= num_iter:
	friends = 0
	total = 0
	case = lines[i].split()
	for c in range(len(case[1])):
		if total<c:
			friends +=1
			total +=1
		total += int(case[1][c])
	#print case
	out.write( 'Case #' + str(i) + ': ' + str(friends) + '\n')
	i+=1

out.close()