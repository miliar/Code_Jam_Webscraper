##################################
##	solve magic trick problem	##
##	the logic is to find the	##
##	intersection of the 2 rows 	##
##	if it returns 1 element		##
##	then that is the solution	##
##	if it returns more than 1	##
##	element then bad magician	##
##	if it returns 0 element		##
##	then user cheated			##
##################################

import sys

def readData(f):
	data = []
	inputs = int(f.readline().rstrip('\n\t\r'))
	count = 0
	rec = []
	matrix = []
	for temp in f:
		temp = temp.rstrip('\n\r\t')
		count = count + 1
		if count == 1:
			rec.append(int(temp))
		elif count <=5:
			matrix.append(temp.split())
		elif count == 6:
			rec.append(matrix)
			matrix = []
			rec.append(int(temp))
		elif count <=9:
			matrix.append(temp.split())
		else:
			matrix.append(temp.split())
			rec.append(matrix)
			data.append(rec)
			count = 0
			matrix = []
			rec = []
	return data	

def result(rec):
	row1 = rec[1][rec[0]-1]
	row2 = rec[3][rec[2]-1]
	out = []
	for val in row1:
		if val in row2:
			out.append(val)
	if len(out) == 1:
		return out[0]
	elif len(out) > 1:
		return 'Bad magician!'
	elif len(out) == 0:
		return 'Volunteer cheated!'
	
def main():
	"""main function
	./magic.py filename"""
	if len(sys.argv)!= 2:
		print 'usage: %run magic.py filename'
		sys.exit(1)
	f = open(sys.argv[1], 'r')
	data = readData(f)
	count = 1
	for rec in data:
		print 'Case #'+str(count)+': '+result(rec)
		count = count + 1
	
	
#call the main program
if __name__ == '__main__':
	main()