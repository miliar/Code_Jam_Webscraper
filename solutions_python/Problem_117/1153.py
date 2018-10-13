import sys

def checkSquare(lawn, n, m, position):
				val = lawn[position[0]][position[1]]
				rowValid = True
				for i in range(n):
								if lawn[i][position[1]] > val:
												rowValid = False
												break
				if rowValid:
								return True

				for j in range(m):
								if lawn[position[0]][j] > val:
												return False
				return True

def isPossible(lawn, n, m):
				#print lawn
				for i in range(n):
								for j in range(m):
												if not checkSquare(lawn, n, m, (i,j)):
																return 'NO'
				return 'YES'


lines = [x.strip() for x in open(sys.argv[1]).readlines()]
numCases = int(lines[0])
lines = lines[1:]

currIdx = 0
for caseNum in range(numCases):
				(n,m) = [int(x) for x in lines[currIdx].split()]
				currIdx += 1

				lawn = [map(int, x.split()) for x in lines[currIdx:currIdx+n]]
				result = isPossible(lawn, n, m)

				print 'Case #%d: %s' % ((caseNum+1), result,)

				currIdx += n
				
