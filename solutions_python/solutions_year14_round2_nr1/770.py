import sys
sys.setrecursionlimit(1100)

cc = int(raw_input().strip())

def dedup(word):
	global count
	ret = ''
	tmp = 0
	cnt = []
	pos = 0
	while(pos < len(word)):
		ret += word[pos]
		now = word[pos]
		tmp = 1
		pos += 1
		while(pos < len(word) and word[pos] == now):
			tmp += 1
			pos += 1
		cnt.append(tmp)
	count.append(cnt[::])
	return ret

def solve(x):
	global count,N
	ret = 0
	for i in range(x):
		summ = 0.0
		for j in count:
			summ += j[i]
		avg = int(round(summ/N))
		for j in count:
			ret += int(abs(avg-j[i]))
	return ret

for ccc in range(1,cc+1):
	print 'Case #' + str(ccc) + ':',
	N = int(raw_input().strip())
	inp = []
	count = []
	ans = 0
	for i in range(N):
		inp.append(raw_input().strip())
	dd = dedup(inp[0])
	for word in inp[1::]:
		if(dedup(word) != dd):
			ans = 'Fegla Won'
#print count,dd
	if(ans == 0):
		ans = solve(len(dd))
	print ans
