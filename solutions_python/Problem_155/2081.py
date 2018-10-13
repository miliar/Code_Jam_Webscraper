import csv
def solve(row):
	max = int(row[0])
	shy = row[1]
	send = 0
	needed = 0
	have = 0
	for i,x in enumerate(shy):
		if have < i:
			send += 1
		needed += int(x)
		have = send + needed
	return str(send)
with open('A-large.in','rb') as file:
	print file.readline()
	x = open('a-sol.txt','w')
	reader = csv.reader(file, delimiter = ' ')
	i = 1
	for row in reader:
		
		y = solve(row)
		x.write('Case #%d: '%i + y+'\n')
		i+=1
	x.close()


