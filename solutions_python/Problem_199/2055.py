fi = open("A-large.in")
fo = open("A-large.out", "w")

line = next(fi)
T = int(line)
for t in range(T):
	line = next(fi)
	[S, K] = line.rstrip().split(' ')
	K= int(K)
	S = [1 if s=='+' else 0 for s in S]
	count = 0
	impossible = False
	for i in range(len(S)-K+1):
		if S[i] == 0:
			count += 1
			for j in range(i, i+K):
				S[j] = 1 - S[j]
	for i in range(len(S)-K+1, len(S)):
		if S[i] == 0:
			count = "IMPOSSIBLE"
			break
			
	fo.write("Case #" + str(t+1) + ": " + str(count) + "\n")

fi.close()
fo.close()
