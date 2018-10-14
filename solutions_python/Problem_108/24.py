from string import lowercase
import sys

rl = sys.stdin.readline
T = int(rl())

def solve(vines):
	for i in range(0, len(vines)):
		if vines[-1]['r']:
			break
		vine = vines[i]
		if vine['r'] == False:
			break
		
		for j in range(i + 1, len(vines)):
			if vines[j]['p'] <= vine['p'] + vine['p'] - vine['m']:
				vines[j]['r'] = True
				vines[j]['m'] = min(vines[j]['m'], max(vines[j]['p'] - vines[j]['l'], vine['p']))
			else:
				break 

for i in range(0, T):
	N = int(rl())
	
	vines = []
	for j in range(0, N):
		inp = map(int, rl().split(' '))
		vines.append({'p': inp[0], 'l': inp[1], 'r': False, 'm': inp[0]})
	D = int(rl())
	vines.append({'p': D, 'l': 0, 'r': False, 'm': D})
	
	vines[0]['r'] = True
	vines[0]['m'] = 0
	solve(vines)
		
	if vines[-1]['r']:
		print 'Case #%d: YES' % (i+1)
	else:
		print 'Case #%d: NO' % (i+1)
