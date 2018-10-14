def isTidy(n):
	strN = str(n)
	if strN == ''.join(sorted(strN)):
		return True
	else:
		return False
		
def testN(N):
	for x in range(N,0,-1):
		if isTidy(x) == True:
			return x
	return -1
	
test = open("B-small-attempt3.in")

test.readline()
case = 1
out = open("B-small-attempt3.out", 'w')
for line in test:
	out.write("Case #{}: {} \n".format(case, testN(int(line))))
	case+=1