import sys
import os
import fileinput

'''

Case #1: X won
Case #2: Draw
Case #3: Game has not completed
Case #4: O won
Case #5: O won
Case #6: O won

'''
def check(rows, c):
	for row in rows:
		if row[0]==c and row[1]==c and row[2]==c and row[3]==c:
			return True

	#diagonal
	if rows[0][0]==c and rows[1][1]==c and rows[2][2]==c and rows[3][3]==c:
		return True
	if rows[0][3]==c and rows[1][2]==c and rows[2][1]==c and rows[3][0]==c:
		return True

	transpose = map(list, zip(*rows))
	for row in transpose:
		if row[0]==c and row[1]==c and row[2]==c and row[3]==c:
			return True	

if __name__ == '__main__':
	lines = []
	for line in fileinput.input():
		if line.strip() == '':
			continue
 		lines.append(line[:-1])

	n = int(lines[0])

	for x in xrange(n):
		prob = lines[x*4+1:x*4+5]
		
		#check for X
		newrows = []
		for row in prob:
			newrows.append(row.replace('T','X'))

		if check(newrows, 'X'):
			sys.stdout.write('Case #{0}: X won\n'.format(x+1))
			continue

		#check for T
		newrows = []
		for row in prob:
			newrows.append(row.replace('T','O'))

		if check(newrows, 'O'):
			sys.stdout.write('Case #{0}: O won\n'.format(x+1))	
			continue

		dot_found = False
		for row in newrows:
			if '.' in row:
				dot_found = True
				break

		if dot_found:
			sys.stdout.write('Case #{0}: Game has not completed\n'.format(x+1))	
			continue		
		else:
			sys.stdout.write('Case #{0}: Draw\n'.format(x+1))	
			continue	
