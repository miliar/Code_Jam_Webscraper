def flip(s,i,k):
	s = list(s)
	for j in range(k):
		s[i+j] = str(int(s[i+j])^1)
	return ''.join(s)

def getFlipNum(s,k):
	queue = []
	statusSet = set()

	slen = len(s)
	flipCount = 0
	status = [s,flipCount]

	queue.append(status)
	statusSet.add(status[0])
	while len(queue) != 0:
		status = queue.pop(0)
		for i in range(slen-k+1):
			nextS = flip(status[0], i, k)
			if isHappy(nextS):
				return status[1]+1
			if nextS not in statusSet:
				statusSet.add(nextS)
				queue.append([nextS,status[1]+1])
	return False

def isHappy(s):
	for i in s:
		if i != '1':
			return False
	return True

if __name__ == '__main__':

	caseNum = int(input())
	
	for i in range(caseNum):
		
		s, k = [s for s in input().split(" ")]
		s = s.replace('+','1')
		s = s.replace('-','0')

		if isHappy(s):
			result = 0;
		else:
			flipNum = getFlipNum(s,int(k))
			if flipNum:
				result = flipNum
			else:
				result = "IMPOSSIBLE"
		print("Case #{}: {}".format(i+1,result))

