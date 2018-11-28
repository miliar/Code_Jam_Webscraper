import copy

T = int(raw_input())

def compare(val, arr):
	for i in arr:
		if i!=val: return 0
	return 1

def hcheck(data, i):
	return compare(1, data[i])

def vcheck(data, j):
	transpose = map(list, zip(*data))
	return compare(1, transpose[j])

def solve(data):
	for row in range(len(data)):
		for col in range(len(data[i])):
			if data[row][col]==1:
				if not (hcheck(data,row) or vcheck(data, col)): return "NO"
	return "YES"

for test in range(T):
	n,m = raw_input().split()
	n,m=int(n),int(m)
	data = []
	for i in range(n):
		data.append(map(int, raw_input().split()))
	print "Case #" + str(test+1) + ": " + solve(data)