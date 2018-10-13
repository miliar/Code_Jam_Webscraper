import sys
import psyco
psyco.full()

def findBasin(basin, i, j, label, graph):
	for e in graph[i][j]:
		if basin[e[0]][e[1]] == 0:
			basin[e[0]][e[1]] = label
			findBasin(basin, e[0], e[1], label, graph)

def main():
	mov = [(-1, 0), (0, -1), (0, 1), (1, 0)]
	t = int(sys.stdin.readline())
	for x in range(1, t+1):
		h, w = [int(i) for i in sys.stdin.readline().split()]
		grid = []
		graph = [[[] for j in range(w)] for i in range(h)]
		basin = [[0]*w for i in range(h)]
		for i in range(h):
			grid.append([int(j) for j in sys.stdin.readline().split()])

		for i in range(h):
			for j in range(w):
				current = grid[i][j]
				besta, bestb = i, j
				for k in mov:
					a, b = i + k[0], j + k[1]
					if a >= 0 and a < h and b >= 0 and b < w:
						if grid[a][b] < current:
							current, besta, bestb = grid[a][b], a, b
				if besta != i or bestb != j:
					graph[i][j].append((besta, bestb))
					graph[besta][bestb].append((i, j))
					
		label = ord('a')
		for i in range(h):
			for j in range(w):
				if basin[i][j] == 0:
					basin[i][j] = label
					findBasin(basin, i, j, label, graph)
					label = label+1
					
		print 'Case #%d:' % x
		for i in range(h):
			line = chr(basin[i][0])
			for j in range(1, w):
				line += ' %c' % chr(basin[i][j])
			print line

main()
