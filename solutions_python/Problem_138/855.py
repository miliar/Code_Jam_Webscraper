with open('input.in','r') as f:
	lines = f.readlines()
f.close

f = open('output.out','w')

tmp = []
for l in lines:
	try: tmp.append(int(l.strip()))
	except ValueError: tmp.append([float(f) for f in l.split()])
lines = tmp

T = lines[0]

for t in range(T):
	C = t*3+1
	B = lines[C]
	n_blocks = lines[C+1]
	k_blocks = lines[C+2]
	n_blocks.sort()
	k_blocks.sort()

	dw_score = 0
	w_score = 0
	cheats = 0
	unused = [True for _ in range(B)]
	for b in reversed(range(B)):
		if n_blocks[b+cheats] > k_blocks[b]: dw_score += 1
		elif n_blocks[cheats] < k_blocks[b]: cheats += 1

	for nb in reversed(range(B)):
		smallest_diff = n_blocks[nb] - k_blocks[0]
		sd_id = 0
		for kb in range(len(k_blocks)):
			diff = n_blocks[nb] - k_blocks[kb]
			if diff < smallest_diff and diff < 0:
				smallest_diff = diff
				sd_id = kb
		if smallest_diff > 0:
			del k_blocks[0]
			w_score += 1
		else:
			del k_blocks[sd_id]

	f.write('Case #'+str(t+1)+': '+str(dw_score)+' '+str(w_score)+'\n')
