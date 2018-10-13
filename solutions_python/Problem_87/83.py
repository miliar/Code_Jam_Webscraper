import sys

cases = int(raw_input())
for case in range(1, cases + 1):
	X, S, R, T, N = [int(i) for i in raw_input().split(' ')]

	ws = []
	last_e = 0
	for walkway in range(N):
		B, E, w = [int(i) for i in raw_input().split(' ')]
		if B > last_e:
			ws.append([S, last_e, B])
		ws.append([S + w, B, E])
		last_e = E

	if last_e < X:
		ws.append([S, last_e, X])

	#print ws

	total = 0
	ws = sorted(ws)
	for w, b, e in ws:
		d = e - b

		if T > 0:
			rs = float(w + R - S)
			best_time = d / rs

			if best_time < T:
				time = best_time
				T -= time
			else:
				pd = rs * T
				time = T + (d - pd) / float(w)
				T = 0
		else:		
			time = d / float(w)
		

		#print b, e, w, time, T
		total += time

	sys.stdout.write("Case #%d: %.9f\n" % (case, total))

