import math

def getTree(N):
	DIR = {}
	for path in range(N):
		buffer = raw_input()
		data = buffer.split("/")
		data.pop(0)
		DIR[buffer] = 1
		current = ""
		for d in data:
			current += "/"+d
			if not(current in DIR): DIR[current] = 1
	return DIR
	

def getMkdir(M,tree):
	ret = 0
	for path in range(M):
		buffer = raw_input().split("/")
		buffer.pop(0)
		current = ""
		for d in buffer:
			current += "/" + d
			if not(current in tree):
				ret += 1
				tree[current] = 1
	return ret

T = int(raw_input())
for test in range(T):
	# Get data here 
	buffer = raw_input().split()
	N , M = int(buffer[0]) , int(buffer[1])
	tree = getTree(N)		
	print("Case #"+str(test+1)+": "+str(getMkdir(M,tree)))