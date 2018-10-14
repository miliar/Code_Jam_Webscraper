import sys
inp = sys.stdin

def read_ints():
	return map(int, inp.readline().split())

T=read_ints()[0]
for t in range(T):
	word, n = inp.readline().split()
	n = int(n)
	L = len(word)
	word = [l not in 'aeiou' for l in word]
	ans = 0
	for i in range(L):
		for j in range(i+n, L+1):
			consec = 0
			for l in range(i,j):
				if word[l]:
					consec += 1
					if consec >= n:
						ans += 1
						break
				else:
					consec = 0
	print "Case #%d: %d" % (t+1, ans)
