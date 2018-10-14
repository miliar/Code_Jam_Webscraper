
import sys

lines = [line.strip() for line in open(sys.argv[1])]
cases = int(lines[0])
lines.remove(lines[0])

class num_pos:
	def __init__(self, num, list):
		self.num = num
		self.list = list

class patt:
	def __init__(self, n, m, mat):
		self.r = n
		self.c = m
		self.mat = mat

def is_way(listin, num):
	if max(listin) <= num:
		return True
	else :
		return False

def get_4_ways(row, col, obj):
	list1 = obj.mat[row][col:]
	list3 = obj.mat[row][:col+1]
	list2 = []
	list4 = []

	for x in range(0, obj.r):
		for y in range(0, obj.c):
			if y == col:
				if x < row:
					list4.append(obj.mat[x][y])
				elif x > row:
					list2.append(obj.mat[x][y])
				elif x == row:
					list2.append(obj.mat[x][y])
					list4.append(obj.mat[x][y])

	val = obj.mat[row][col]
	
	if (is_way(list1,val) and is_way(list3,val)) or (is_way(list2,val) and is_way(list4,val)):
		return "YES"
	else :
		return "NO"



def process(obj):
	#for small dataset only: 
	for x in range(0, obj.r):
		for y in range(0, obj.c):
			ret = get_4_ways(x,y,obj)
			if ret == "NO":
				return "NO"

	return "YES"

case_number = 1
row_number = 1
for case_number in range(1,cases+1):
	row = lines[row_number-1].split(" ")[0]
	col = lines[row_number-1].split(" ")[1]
	obj	= patt(int(row), int(col), [])
	
	matrix = lines[row_number:row_number+int(row)]
	row_number += int(row)+1
	count = 0
	for line in matrix:
		obj.mat.append(line.split(" "))
		if count == int(row):
			break
		count += 1

	state = process(obj)
	print "Case #" + str(case_number) + ": " + state
	case_number += 1
