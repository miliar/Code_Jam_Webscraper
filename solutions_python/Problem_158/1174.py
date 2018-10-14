import sys

'''

Note that 0, 1, 2 etc are placeholders for square 0-15 respectively 

[0, 1, 2, 3]
[4, 5, 6, 7]
[8, 9, 10, 11]
[12, 13, 14, 15]
'''

[0, 1, 4, 5]
graph = dict()

graph[0] = []

# Graph 1 can have one square at 0 
graph[1] = [ [0] ]

# Graph 2 
graph[2] = [ [0, 1] ]

# Graph 3
graph[3] = [ [0, 1, 2], [0, 1, 4] ]

# Graph 4
graph[4] = [ [0,1,4,5], [0,1,2,4], [0,1,2,5], [0,1,5,6],[0,1,2,3] ]


def inverse(pt):
	return (sq*4 % 4)

def generateRC(R, C):
	rc = []
	v = 0
	if R > C:
		R, C = C, R
	for r in range(R):
		for c in range(C):
			rc.append(v)
			v+=1
		v = (r+1) * 4
	return rc

def convert(lis):
	rc = []
	for i in range(0, 16):
		rc.append(False)

	for l in lis:
		rc[l] = True
	
	return rc


def compare(rc, graph):
	for pts in graph:
		for p in pts:
			if(rc[p] != True):
				return False
	return True


f = sys.stdin
if len(sys.argv) >= 2:
    fn = sys.argv[1]
    if fn != '-':
        f = open(fn)

t = int(f.readline())
for tc in range(0,t):
	arr = f.readline().split()
	X,R,C = int(arr[0]), int(arr[1]), int(arr[2])
	
	winner = ''

	if (R*C) % X != 0:
		winner = 'RICHARD'
	else:
		if X == 1:
			winner = 'GABRIEL' 
		if X == 2:
			if R*C % X == 0:
				winner = 'GABRIEL'
			else:
				winner = 'RICHARD'
		if X == 3:
			if R == 1 or C == 1:
				winner = 'RICHARD'
			else:
				winner = 'GABRIEL'
		if X == 4:
			if R <= 2 or C <= 2:
				winner = 'RICHARD'
			else:
				winner = 'GABRIEL'
	print "Case #%d: %s" % (tc+1, winner)

