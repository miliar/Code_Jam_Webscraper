import copy

def readInts():
    return [int(x) for x in raw_input().strip().split()]

def blue4(arr):
    for i in xrange(len(arr)-1):
	for j in xrange(len(arr[0])-1):
	    if (arr[i][j] == '#'):
		if (arr[i+1][j] == '#' and arr[i][j+1]=='#' and arr[i+1][j+1]=='#'):
		    arr[i][j] = '/'
		    arr[i][j+1] = '\\'
		    arr[i+1][j] = '\\'
		    arr[i+1][j+1] = '/'
		    return (True,arr)
    return (False,arr)
def disp(arr):
    for row in arr:
	    print ''.join(row)
	    

n = readInts()[0]
for i in xrange(n): #for each case 
    [r,c] = readInts()
    arr = []
    arr = [list(raw_input()) for _ in xrange(r)]
    flag = True
    while (flag):
	(flag,arr) = blue4(arr)
    flag = True
    for row in arr:
	for cell in row:
	    if (cell == '#'):
		flag = False
    print "Case #%d:"%(i+1)
    if (flag):
	disp(arr)
    else:
	print "Impossible"
	
	
	