import sys
import psyco
psyco.full()

def main():
	t = int(sys.stdin.readline())
	for x in range(1, t+1):
		line = ' ' + sys.stdin.readline().strip()
		w = ' welcome to code jam'
		n, m = len(line), len(w)
		res = [[0]*m for i in range(n)]
	
		for j in range(m):
			res[0][j] = 0
		for i in range(n):
			res[i][0] = 1
		for i in range(1, n):
			for j in range(1, m):
				res[i][j] = res[i-1][j]
				if line[i] == w[j]:
					res[i][j] += res[i-1][j-1]
		print 'Case #%d: %04d' % (x, res[n-1][m-1] % 10000)

main()
