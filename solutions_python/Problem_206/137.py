ntc = int(input())

for tc in range(ntc):
	d, nhorses = map(int, input().split())

	mi_v = -1
	for i in range(nhorses):
		si, vi = map(int, input().split())
		cur_v = vi*d/(d-si)
		if mi_v == -1 or cur_v < mi_v: 
			mi_v = cur_v

	print('Case #{}: {}'.format(tc+1, mi_v))
	