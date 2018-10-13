def sol(S):
	c = S[0]
	s_idx = 0
	c_idx = 0
	for n in S[1:]:
		if n >= c:
			c_idx+=1
			if n > c:
				s_idx += 1
			c = n
		else:
			break

	if c_idx < len(S)-1:
		S[s_idx] -= 1
		S[s_idx+1:] = [9] * len(S[s_idx+1:])

	return S[1:] if S[0] == 0 else S

TT = int(raw_input())

for T in range(1,TT+1):
	S = map(int, list(raw_input()))
	print "Case #{}: {}".format(T, ''.join(map(str, sol(S))))