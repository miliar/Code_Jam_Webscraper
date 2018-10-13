import numpy as np

def main():
	fname = 'A-large.in'
	fname_out = 'A-large.out'
	fout = open(fname_out, 'wt')
	with open(fname) as fin:
		T = int(fin.readline().strip())
		print("num of test: %d" % T)
		for t in range(1, T+1):
			R, C = map(int, fin.readline().strip().split(' '))
			cakes = []
			for r in range(R):
				cakes.append(list(fin.readline().strip()))
			#print(cakes)
			alp = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
			for c in alp:
				coor = []
				for y in range(R):
					for x in range(C):
						if c == cakes[y][x]:
							coor.append((y,x))
				for i in range(len(coor)):
					for j in range(i+1, len(coor)):
						min_y = min(coor[i][0], coor[j][0])
						min_x = min(coor[i][1], coor[j][1])
						max_y = max(coor[i][0], coor[j][0])
						max_x = max(coor[i][1], coor[j][1])
						for y in range(min_y, max_y+1):
							for x in range(min_x, max_x+1):
								cakes[y][x] = c
			#print(cakes)
			cakes = np.array(cakes)
			#for a in alp:
			for i in range(R):
				for j in range(C):
					a = cakes[i][j]
					minx, miny, maxx, maxy = 30, 30, -1, -1
					for r in range(R):
						for c in range(C):
							if cakes[r][c] == a:
								minx = min(minx, c)
								miny = min(miny, r)
								maxx = max(maxx, c)
								maxy = max(maxy, r)
					if 30 in [minx, miny] or -1 in [maxx, maxy]:
						continue
					x = minx-1
					while x >= 0 and all('?' == item for item in cakes[miny:maxy+1,x]):
						cakes[miny:maxy+1,x] = a
						minx -= 1
						x -= 1
					x = maxx+1
					while x < C and all('?' == item for item in cakes[miny:maxy+1,x]):
						cakes[miny:maxy+1,x] = a
						maxx += 1
						x += 1
					y = miny-1
					while y >= 0 and all('?' == item for item in cakes[y,minx:maxx+1]):
						cakes[y,minx:maxx+1] = a
						miny -= 1
						y -= 1
					y = maxy+1
					while y < R and all('?' == item for item in cakes[y,minx:maxx+1]):
						cakes[y,minx:maxx+1] = a
						maxy += 1
						y += 1

			for r in range(R):
				for c in range(C):
					if cakes[r][c] == '?':
						print(t)
						print(cakes)

			fout.write("Case #%d:\n" % (t))
			for r in range(R):
				for c in range(C):
					fout.write('%s'%cakes[r][c])
				fout.write('\n')



if __name__ == '__main__':
	main()
