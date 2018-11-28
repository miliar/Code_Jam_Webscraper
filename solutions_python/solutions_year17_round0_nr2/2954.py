import sys

total = int(sys.stdin.readline())

def isTidy(n):
	l = len(n)
	for i in range(0,l-1):
		if(n[i]>n[i+1]):
			return False
	return True

def findTidy(n):
	l = len(n)
	i = 0
	lsans = list(n)
	if lsans[l-1]=='\n':
		lsans = lsans[0:l-1]
		l = l-1
	if isTidy(lsans):
		return "".join(lsans)
	while i<l-1:
		if(n[i]>n[i+1]):
			break
		else:
			i=i+1
	while i>0:
		if(n[i] == n[i-1]):
			i = i-1
		else:
			break
	lsans[i] = str(int(lsans[i])-1)
	for j in range(i+1,l):
		lsans[j] = '9'
	i = 0
	while i<len(lsans):
		if lsans[i]=='0':
			i=i+1
		else:
			break
	ans = "".join(lsans[i:])
	return ans


for i in range (1,total+1):
	n = sys.stdin.readline()
	# num = int(n)
	# for j in range (0,num):
	# 	if(isTidy(str(num-j))):
	# 		print("Case #%s:"%i,num-j)
	# 		break
	ans = findTidy(n)
	print("Case #%s:"%i,ans)