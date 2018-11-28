try:
	nTests = int(raw_input())

	for test in xrange(1, nTests+1):
		n, m = map(int, raw_input().split())
		lawn = [map(int, raw_input().split()) for _ in xrange(n)]

		fail = True

		for l in xrange(n):
			for c in xrange(m):
				height = lawn[l][c]

				for k in xrange(m):
					if height < lawn[l][k]:
						break
				else:
					continue

				for k in xrange(n):
					if height < lawn[k][c]:
						break
				else:
					continue
				break
			else:
				continue
			break
		else:
			fail = False

		print "Case #%d: %s" % (test, "NO" if fail else "YES")

except EOFError:
	pass
