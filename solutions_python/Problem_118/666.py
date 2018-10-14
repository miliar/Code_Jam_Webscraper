def isPalindrome(num):
	hold1 = str(num)
	hold2 = hold1[::-1]
	return hold1 == hold2
	
def isFairSquare(num):
	if not isPalindrome(num):
		return False
	if not isPalindrome(num**2):
		return False
	return True

FSq = []
for i in range(10**7):
	if isFairSquare((i+1)):
		FSq.append((i+1)**2)


f = open('C-large-1.in.txt','r')
g = open('output.txt', 'w')
C = int(f.readline())
for i in range(C):
	count = 0
	A, B = f.readline().strip().split(' ')
	for j in range(len(FSq)):
		if FSq[j] >= int(A) and FSq[j] <= int(B):
			count += 1
		elif FSq[j] > int(B):
			break
	g.write('Case #%d: %d\n' % (i+1,count))
			