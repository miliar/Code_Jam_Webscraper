import copy

def compare(arr):
	val = arr[0]
	for i in arr:
		if i!=val: return 0
	return 1

def linecheck(data, mask):
	res = 0
	for row in data:
		res = res | compare([mask, row[0]&mask, row[1]&mask, row[2]&mask,row[3]&mask])
	return res

def diacheck(data, mask):
	i = 0
	first = compare([mask, data[0][0]&mask, data[1][1]&mask, data[2][2]&mask, data[3][3]&mask])
	second = compare([mask, data[0][3]&mask, data[1][2]&mask, data[2][1]&mask, data[3][0]&mask])
	return first|second

def nonull(data):
	for row in data:
		for item in row:
			if item==0: return 0
	return 1

def solve(data):
	transpose = map(list, zip(*data))
	if diacheck(data, 1) or linecheck(data, 1) or linecheck(transpose, 1):
		return "X won"
	elif diacheck(data, 2) or linecheck(data, 2) or linecheck(transpose, 2):
		return "O won"
	elif nonull(data):
		return "Draw"
	else:
		return "Game has not completed"

def convert(c):
	if c=='X':
		return 1
	elif c=='O':
		return 2
	elif c=='T':
		return 3
	else:
		return 0

n = int(raw_input())

i=0
while i<n:
	if i>0: raw_input()
	l1,l2,l3,l4 = raw_input(),raw_input(),raw_input(),raw_input()
	data = [map(convert, list(l)) for l in [l1,l2,l3,l4]]
	print "Case #" + str(i+1) + ": " + solve(data)
	i = i + 1