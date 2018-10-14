def lawnMoler(pattern,n,m):
	for x in range(n):
		for y in range(m):
			a = True
			b = True
			for i in range(n):
				if(pattern[i][y]>pattern[x][y]):
					a = False
			for i in range(m):
				if(pattern[x][i]>pattern[x][y]):
					b = False
			if not (a or b):
				return False
	return True

def boolstring(x):
	if x:
		return "YES"
	return "NO"

with open('input.in') as f:
    lines = f.read().splitlines()
    T = int(lines[0])
 
    line = 1
    for i in range(T):
    	dimensions = lines[line].split(' ')
    	n = int(dimensions[1])
    	m = int(dimensions[0])
    	line = line + 1
    	pattern = []
    	for y in range(m):
    		k = []
    		raw = lines[line].split(' ')
    		for x in range(n):
    			k.append(raw[x])
    		pattern.append(k)
    		line = line + 1
    	print 'Case #'+str(i+1)+": "+boolstring(lawnMoler(pattern,m,n))