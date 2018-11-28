import itertools

def convert(i,j, C):
	return j + C*i
	
def revert(n, C):
	j = n % C
	i = n/C
	return i,j
	
def neighbors(i,j, R, C):
	
	indices = []
	#left one if exists
	if j >= 1 and C >=2:
		indices.append(convert(i, j-1, C))
	#right one if exists	
	if j <= C-2 and C>=2:
		indices.append(convert(i, j+1, C))
		
	#under
	if i >= 1 and R >= 2:
		indices.append(convert(i-1, j, C))
		
	#over
	if i <= R-2 and R >= 2:
		indices.append(convert(i+1, j, C))
	return indices


def solve(R, C, N):
	
	ans = 987654321
	
	for each in itertools.combinations(range(R*C), N):
		cand = 0
		for i in each:
			x,y = revert(i, C)
			walls = neighbors(x,y, R, C)
			for neighbor in walls:
				if neighbor in each:
					cand += 1
		ans = min(ans, cand/2)
	return ans



f = open("B-small-attempt0.in", 'r')
f2 = open("outputNeighborSmall.txt", 'w')	
t = int(f.readline())
for i in xrange(t):
	s = "Case #" + str(i+1) + ": "
	
	l = map(int, f.readline().split())
	R, C, N = l[0], l[1], l[2]
	print R, C, N
	if i == t-1:
		f2.write(s+str(solve(R,C,N)))
	else:
		f2.write(s+str(solve(R,C,N))+'\n')

f.close()
f2.close()
