def drawCircle(whiter, t, cnt):
	area = (whiter + 1) ** 2 - whiter ** 2
	if t < area:
		return cnt
	else:
		return drawCircle(whiter + 2, t - area, cnt + 1)


#f = open('sample.txt', 'r')
f = open ('A-small-attempt0.in', 'r')
f2 = open('output.txt', 'a')

inputNumber = 1
firstFlg = 1
for line in f:
	line = line.split()
	if firstFlg:
		numOfInput = int(line[0])
		firstFlg = 0
	else:
		r = int(line[0])    
		t = int(line[1])

		result = drawCircle(r, t, 0)
		f2.write('Case #' + str(inputNumber) + ': ' + str(result) + '\n')
		inputNumber = inputNumber + 1

f2.close()
f.close()