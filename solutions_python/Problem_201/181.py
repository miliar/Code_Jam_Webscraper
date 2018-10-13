import heapq

def adnc(nc, v, ad):
	if v == 0: return
	k = (v // 2, (v-1) // 2)
	nc[k] = nc.get(k, 0) + ad

TC = int(input())
for tc in range(TC):
	N, K = map(int, input().split())
	K -= 1
	c = {(N // 2, (N-1) // 2): 1}
	stg = 0
	while K >= (1<<stg):
		nc = {}
		for k, v in c.items():
			adnc(nc, k[0], v)
			adnc(nc, k[1], v)
		c = nc
		K -= (1<<stg)
		stg += 1
	ks = list(c.keys())
	ks.sort(reverse=True)
	for k in ks:
		if K >= c[k]:
			K -= c[k]
		else:
			print('Case #%d: %d %d' % (tc+1, k[0], k[1]))
			break
