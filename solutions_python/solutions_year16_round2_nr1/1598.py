Number_Strings = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

def isExist(s, d):
	tmpD = {}
	for c in s:
		if c in tmpD: tmpD[c] += 1
		else: tmpD[c] = 1
	for k in tmpD:
		if k not in d or tmpD[k] > d[k]: return False
	return True

def recur(d, i, ans):
	if len(d) == 0:
		global globalAns
		globalAns = ans
		return
	print(d, i, ans)
	for j in range(i, len(Number_Strings)):
		if isExist(Number_Strings[j], d):
			for c in Number_Strings[j]:
				d[c] -= 1
				if d[c] == 0: del d[c]
			ans += str(j)
			recur(d, j, ans)
			for c in Number_Strings[j]:
				if c in d: d[c] += 1
				else: d[c] = 1
			ans = ans[:len(ans)-1]


def solve(s):
	d = {}
	for c in s:
		if c in d: d[c] += 1
		else: d[c] = 1
	global globalAns
	#print(d)
	globalAns = ""
	recur(d, 0, "")
	return globalAns

def main():
	inFile = open("A-small-attempt0.in", "r")
	outFile = open("A-small-attempt0.out", "w")
	T = int(inFile.readline())
	for i in range(1, T+1):
		s = inFile.readline()
		s = s[:len(s)-1]
		outFile.write("Case #%d: %s\n" % (i, solve(s)))
main()
