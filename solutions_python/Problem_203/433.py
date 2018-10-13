import numpy as np

T = int(input())
for j in range(T):
	(R, C) = map(int, input().split(" "))
	cake = np.empty((R,C), dtype=str)
	for r in range(R):
		cake[r,:] = list(input())
	for r in range(R):
		prev_char = None
		for c in range(C):
			if cake[r,c] == '?':
				if prev_char is not None:
					cake[r,c] = prev_char
			else:
				if prev_char is None:
					cake[r,:c] = cake[r,c]
				prev_char = cake[r,c]
	prev_row = None
	for r in range(R):
		if np.all(cake[r,:] == '?'):
			if prev_row is not None:
				cake[r,:] = cake[prev_row,:]
		else:
			if prev_row is None:
				cake[:r,:] = np.tile(cake[r,:], (r,1))
			prev_row = r
	print("Case #%d:" % (j+1,))
	for r in range(R):
		print("".join(cake[r,:]))
