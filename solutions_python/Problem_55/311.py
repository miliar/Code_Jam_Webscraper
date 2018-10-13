import sys

def money(R, k, N, l):
	patterns = [(0,-1)]*N # cost, next
	prev = 0
	cur = 0
	while patterns[cur][0] == 0:
		w = 0
		u = 0
		while True:
			if w+l[cur] > k or u == N: # wait next
				patterns[prev] = (w, cur)
				prev = cur
				break
			else: # you may ride
				w += l[cur]
				u += 1
				cur = (cur + 1)%N
	cur = 0
	total = 0
	for _ in range(0, R): # faster
		total += patterns[cur][0]
		cur = patterns[cur][1]
	return total

f = sys.argv[1]
fin = open(f)
fout = open(f.replace('in','out'), 'w')
T = int(fin.next())
for i in range(0, T):
	[R, k, N] = map(int, fin.next().split(' '))
	l = map(int, fin.next().split(' '))
	fout.write("Case #%d: %d\n"%(i+1, money(R, k, N, l)))

