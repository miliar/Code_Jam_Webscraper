def isTidy(num):
	strNum=str(num)
	l = len(strNum)
	for i in range(l-1):
		if int(strNum[i+1])<int(strNum[i]):
			return False
	return True

def countReverse(j,num):
	for i in reversed(range(int(num)+1)):
		if isTidy(i):
			print "Case #{}: {}".format(j,i)
			return i

t = int(raw_input())
for i in xrange(1,t+1):
	t = raw_input()
	countReverse(i,t)


