import sys

def readInts(f):
	ret = list(map(int, f.readline().strip().split(" ")))
	if len(ret) == 1: return ret[0]
	else: return ret
	#return ret
	
def readWords(f):
	ret = list(f.readline().strip().split(" "))
	if len(ret) == 1: return ret[0]
	else: return ret
	
def changeChar(s, i, c):
	s = s[:i] + c + s[i+1:]
	return s
	
def swapString(s, i, j):
	tmp = s[i]
	s = s[:i] + s[j] + s[i+1:]
	s = s[:j] + tmp + s[j+1:]
	return s

fi = open("input.txt", "r")
fo = open("output.txt", "w")

c = readInts(fi)
for tc in range(1, c+1):
	r, k, n = readInts(fi)
	g = readInts(fi)
	if n == 1:
		tmp = g
		g = [tmp]
	
	ans = 0
	for i in range(1, r+1):
		cap = 0
		j = 0
		t = 0
		while cap + g[j] <= k:
				cap += g[j]
				tmp = g.pop(0)
				g.append(tmp)
				
				t += 1
				if t >= n:
					break
		ans += cap
			
	fo.write("Case #%d: %d\n" % (tc, ans))