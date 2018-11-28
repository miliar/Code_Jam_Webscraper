
def getTestCases():
	n = int(raw_input())
	l = []
	for i in range(0,n):
		l.append(int(raw_input()))
	return n,l

def isTidy(number):
	l = [int(d) for d in str(number)]
	for i in range(0,len(l)-1):
		if l[i] > l[i+1]:
			return False
	return True

def findTidy(number):
	while not isTidy(number):
		l = [int(d) for d in str(number)]
		for i in range(len(l)-1,0,-1):
			if l[i] < l[i-1]:
				l[i-1] -= 1
				for x in range(i,len(l)):
					l[x] = 9
		number = int("".join(map(str,l)),10)
	return number

if __name__ == '__main__':
	n,l = getTestCases()
	print(n)
	print(l)
	for i in range(0,n):
		print('Case #'+str(i+1)+': '+ str(findTidy(l[i])))