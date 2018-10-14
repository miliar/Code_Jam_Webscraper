y, z = 0, 0

def find_left(i, used):
	cnt = 0
	for j in range(i - 1, 0, -1):
		if not used[j]:
			cnt += 1
		else:
			break
	return cnt

def find_right(i, used):
	cnt = 0
	for j in range(i + 1, len(used)):
		if not used[j]:
			cnt += 1
		else:
			break
	return cnt

def find_stall(used, a):
	global y, z
	stalls = []
	mi = 0
	for i in range(1, len(a)):
		if not used[i] and min(a[i]) > min(a[mi]):
			mi = i
	#print('mi:', mi)
	for i in range(1, len(a)):
		if not used[i] and  min(a[mi]) == min(a[i]):
			stalls.append(i)
	#print('stalls:', stalls)
	if len(stalls) == 1:
		y = max(a[stalls[0]])
		z = min(a[stalls[0]])
		return stalls[0]
	
	mx = 0
	for s in stalls:
		if not used[s] and  max(a[mx]) < max(a[s]):
			mx = s
	#print('mx:', mx)
	mxStalls = []
	for s in stalls:
		if not used[s] and  max(a[mx]) == max(a[s]):
			mxStalls.append(s)
	#print('mxstalls', mxStalls)
	y = max(a[mxStalls[0]])
	z = min(a[mxStalls[0]])
	return mxStalls[0]

def recalculate(used, vals):
	ans = [[0,0]] * len(used)
	
	for i in range(1, n+1):
		ans[i] = [find_left(i, used), find_right(i, used)]
	
	return ans

t = int(input())
for o in range(t):
	n, k = map(int, input().split())
	used = [False] * (n + 2)
	used[0] = True
	used[-1] = True
	vals = [[0, 0]] * (n + 2)

	
	vals = recalculate(used, vals)
	#print(vals)
	for _ in range(k):
		y = -1
		z = 1000000000000000
		#print(vals)
		pos = find_stall(used, vals)
		#print(_, 'found position', pos)
		used[pos] = True
		vals = recalculate(used, vals)
		#print('After recalculation', vals)
	
	print('Case #{0}: {1} {2}'.format(o + 1, y, z))
