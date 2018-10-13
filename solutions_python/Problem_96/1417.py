filein = open('./B-small-attempt1.in', 'r')
fileout = open('./B-small-attempt1.out', 'w')

# filein = open('./test')
# fileout = open('./testout', 'w')

def min(a, b):
	if a < b:
		return a
	else:
		return b

lines = filein.readlines()
T = lines[0]
tempRows = []
for i, line in enumerate(lines):
	if not i == 0:
		tempRows.append(line.split(' '))

rows = []
for i, r in enumerate(tempRows):
	rows.append([])
	for j in r:
		rows[i].append(int(j))

for j, row in enumerate(rows):
	surprises = 0
	toAppend = 0
	p = row[2]
	for i in range(3, len(row)):
		if p <= row[i]/3:
			toAppend += 1
		elif row[i] > 1:
			if row[i]%3 == 0:
				if p == row[i]/3 + 1:
					surprises += 1
			elif row[i]%3 == 1:
				if p == row[i]/3 + 1:
					toAppend += 1
			else:
				if p == row[i]/3 + 1:
					toAppend += 1
				elif p == row[i]/3 + 2:
					surprises += 1
	toAppend += min(surprises, row[1])
	rows[j].append(toAppend)

for i, row in enumerate(rows):
	fileout.write("Case #" + str(i+1) + ": " + str(row[-1]) + "\n")

filein.close()
fileout.close()