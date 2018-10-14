def findRes(flag, left, right):
	mid = left + (right - left)/2
	if right - left <= 2:
		flag[mid] = 1
		return 0, 0, mid

	if flag[mid] != 0:
		maxL, minL, mL = findRes(flag, left, mid)
		maxR, minR, mR = findRes(flag, mid, right)
		return (maxL, minL, mL) if abs(maxL+minL)>=abs(maxR+minR) else (maxR, minR, mR)
	else:
		return right-mid-1, mid-left-1, mid


inData  = open('small.in','r')
outData = open('small.out','w')

lines = int(inData.readline())

for line in range(1,lines+1):
	data = inData.readline().split()
	N = int(data[0])
	K = int(data[1])
	flag = [1]
	flag.extend([0] * N)
	flag.extend([1])

	for i in range(K):
		maxN, minN, mid = findRes(flag, 0, N+1)
		flag[mid] = 1

	outData.write('Case #%d: %d %d\n' % (line, maxN, minN))

inData.close()
outData.close()





