C = int(input())
for cc in range(C):
	N, M = map(int, raw_input().split(' '))
	tree = {}
	for i in range(N):
		folders = raw_input().split('/')
		where = tree
		for i in folders:
			if i:
				if not i in where.keys():
					where.update({i: {}})
				where = where[i]
	res = 0
	for i in range(M):
		folders = raw_input().split('/')
		where = tree
		for i in folders:
			if i:
				if not i in where.keys():
					where.update({i: {}})
					res += 1
				where = where[i]
	print "Case #%d: %d"%(cc+1, res)