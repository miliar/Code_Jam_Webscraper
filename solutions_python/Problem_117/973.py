def test(grass, r, c):
	i = 0
	while(i<r):
		j = 0
		while(j < c):
			k = 0
			problem = False
			while(k<r):
				if(k != i):
					if(int(grass[i][j]) < int(grass[k][j])):
						problem = True
						break
				k += 1
			k = 0
			while(k<c):
				if(not problem):
					break
				if(k != j):
					if(int(grass[i][j]) < int(grass[i][k])):
						return "NO"
				k += 1
			j += 1
		i += 1
	return "YES"

if __name__ == "__main__":
	CT = int(raw_input())
	for i in range(CT):
		N,M = raw_input().split()
		N = int(N)
		M = int(M)
		grassField = []
		for j in range(N):
			grassField.append(raw_input().split())
		print "Case #"+str(i+1)+": "+test(grassField, int(N), int(M))