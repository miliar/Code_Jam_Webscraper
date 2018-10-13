from collections import deque


T = int(input())

for t in range(1, T+1):
	S, K = input().split()
	K = int(K)

	Q = deque()
	Q.append((0, S))

	V = set()

	while Q:
		d, s = Q.popleft()

		if s in V:
			continue

		V.add(s)

		if s.count('-') == 0:
			print('Case #%s: %s' % (t, d))
			break

		for i in range(0, len(s) - K + 1):
			sl = s[i:i+K]
			#print(sl)
			if sl.count('-') == 0:
				continue


			ns = s[:i] + ''.join(['+' if c == '-' else '-' for c in sl])
			Q.append((d + 1, ns + s[i+K:]))


	else:
		print('Case #%s: IMPOSSIBLE' % t)
