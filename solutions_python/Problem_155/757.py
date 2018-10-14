fi = open('/home/pi/Downloads/A-large.in', 'r')
n = int(fi.readline())
ans = []
def sOv(sMax, iStr):
	minFr = 0
	count = 0
	for k in range(sMax + 1):
		# print 'in loop ' + str(k) + ' '
		# print str(count) + ' ' + str(count < k)
		if iStr[k] != 0:
			if count < (k):
				minFr += 1
				count += 1
		count += int(iStr[k])
	return minFr
# print sOv(6 , '0000001')
ctr = n
while ctr > 0:
	strInput = fi.readline()
	sMax, iStr = strInput.split()
	ans.append(sOv (int(sMax), iStr))
	ctr -= 1
fo = open('/home/pi/Downloads/Lout.txt', 'w')
for i in range(n):
	fo.write('Case #' + str(i + 1) + ': ' + str(ans[i]) + '\n')
fo.close()
