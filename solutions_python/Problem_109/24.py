import sys
	
rl = sys.stdin.readline
T = int(rl())

for i in range(1, T + 1):
	N, W, L = map(int, rl().split(' '))
	r = map(int, rl().split(' '))
	pos = [{'x': 0, 'y': 0}] * N
	mats = [{'x': 0, 'y': 0, 'w': W, 'l': L}]
	
	def get_max_idx():
		m = 0
		res = 0
		for i in range(0, len(r)):
			if r[i] > m:
				res = i
				m = r[i]
				
		return res
	
	def alloc(p):
		for idx in range(0, len(mats)):
			mat = mats[idx]
			if (mat['w'] <= 0 or mat['l'] <= 0):
				continue
			if ((mat['w'] >= r[p] * 2 or mat['x'] == 0) and (mat['l'] >= r[p] * 2 or mat['y'] == 0)):
				x = mat['x'] + r[p]
				y = mat['y'] + r[p]
				rx = r[p] * 2
				ry = r[p] * 2
				if mat['x'] == 0:
					x = 0
					rx = r[p]
				if mat['y'] == 0:
					y = 0
					ry = r[p]
				
				pos[p] = {'x': x, 'y': y}
				if mat['w'] > mat['l']:
					mats.append({'x': mat['x'] + rx, 'y': mat['y'], 'w': mat['w'] - rx, 'l': mat['l']})
					mats[idx] = {'x': mat['x'], 'y': mat['y'] + ry, 'w': min(mat['w'], rx), 'l': mat['l'] - ry}
				else:
					mats.append({'x': mat['x'], 'y': mat['y'] + ry, 'w': mat['w'], 'l': mat['l'] - ry})
					mats[idx] = {'x': mat['x'] + rx, 'y': mat['y'], 'w': mat['w'] - rx, 'l': min(mat['l'], ry)}
				r[p] = -r[p]
				break
	
	for j in range(0, N):
		idx = get_max_idx()
		alloc(idx)
	
	res = 'Case #%d:' % (i)
	for j in range(0, N):
		res = res + ' %d.0 %d.0' % (pos[j]['x'], pos[j]['y'])
	
	print res
