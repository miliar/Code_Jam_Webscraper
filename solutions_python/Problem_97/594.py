import sys
input = sys.stdin.readlines()

T = int(input[0][:len(input[0])-1])

for i in range(1, T+1):
	Tcase = input[i]
	if input[i][len(input[i])-1] == '\n':
		Tcase = input[i][:len(input[i])-1]
	Tcase = Tcase.split(' ')
	A = int(Tcase[0])
	B = int(Tcase[1])
	NoD = len(str(A))
	count = 0
	for m in range(A,B+1):
		mStr = str(m)
		tmpnList = []
		for breakPt in range(1,NoD+1):
			n = int(mStr[breakPt:]+mStr[:breakPt])
			if (n > m) and (n <= B):
				tmpnList.append(n)
		tmpnList = sorted(tmpnList)
		last = -1
		for n in tmpnList:
			if n != last:
				count += 1
				last = n
	print 'Case #' + str(i) + ': ' + str(count)
