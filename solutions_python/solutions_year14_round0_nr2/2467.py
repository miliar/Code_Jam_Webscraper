def estimate(C, F, X):
	cookiesPerSecond = 2.0
	minTime = X / cookiesPerSecond + 1
	currentTime = 0.0
	estimatedTime = currentTime + X / cookiesPerSecond
	while estimatedTime < minTime:
		minTime = estimatedTime
		currentTime += C / cookiesPerSecond
		cookiesPerSecond += F
		estimatedTime = currentTime + X / cookiesPerSecond
	return minTime

fin = open('B-large.in', 'r')
fout = open('out.txt', 'w')
T = int(fin.readline())
for i in range(1, T + 1):
	C, F, X = [float(x) for x in fin.readline().split()]
	fout.write('Case #' + str(i) + ': %.7f' % estimate(C, F, X) + '\n')
fin.close()
fout.close()