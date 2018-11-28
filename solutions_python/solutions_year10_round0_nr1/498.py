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
	n, k = readInts(fi)
	
	dp = [0]*50
	
	dp[1] = 1
	for i in range(2, n+1):
		dp[i] = (dp[i - 1] * 2) + 1
	
	ans = "OFF"
	if int((k - dp[n]) / (dp[n] + 1)) * (dp[n] + 1) == k - dp[n]:
		ans = "ON"
	fo.write("Case #%d: %s\n" % (tc, ans))