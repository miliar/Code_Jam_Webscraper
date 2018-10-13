palindromicList = []

def PalindromicReverse(half):
	halfRVS = ""
	for c in half:
		halfRVS = c + halfRVS
	return halfRVS

def PalindromicJudge(pal):
	if  (pal == PalindromicReverse(pal)):
		return 1
	else:
		return 0

def palindromic(palindromicList):
	for i in range(1,5):
		n = pow(10,i-1);
		m = pow(10,i)-1;
		for j in range(n,m+1):
			palindromicHalfStr = str(j)
			palindromicHalfRevStr = PalindromicReverse(palindromicHalfStr)
			palindromicStr = palindromicHalfStr[:-1] + palindromicHalfRevStr
			palindromicList.append(int(palindromicStr))
		for j in range(n,m+1):
			palindromicHalfStr = str(j)
			palindromicHalfRevStr = PalindromicReverse(palindromicHalfStr)
			palindromicStr = palindromicHalfStr + palindromicHalfRevStr
			palindromicList.append(int(palindromicStr))

palindromicList = []
palindromic(palindromicList)
Ans = []

for pal in palindromicList:
	palSQR = pal*pal
	if (PalindromicJudge(str(palSQR))):
		# print palSQR
		Ans.append(palSQR)

s = raw_input()
s = int(s)
for item in range(1,int(s)+1):
	line = raw_input()
	n,m = line.split(' ')
	n = int(n)
	m = int(m)
	result = 0
	for pal in Ans:
		if pal>=n and pal<=m:
			result += 1
	print "Case #%d: %d" % (item ,result)

