
colorList = ['R', 'O', 'Y', 'G', 'B', 'V']

def canBe(a, b):
	if ((a == 0 or a == 1 or a == 5) and (b == 0 or b == 1 or b == 5)):
		return False
	if ((a == 1 or a == 2 or a == 3) and (b == 1 or b == 2 or b == 3)):
		return False
	if ((a == 3 or a == 4 or a == 5) and (b == 3 or b == 4 or b == 5)):
		return False

	return True

def _main():
	N, R, O, Y, G, B, V = raw_input().split(' ')
	n = int(N)
	color = [int(R), int(O), int(Y), int(G), int(B), int(V)]
	colorBis = [color[1] + color[0] + color[5], color[1] + color[2] + color[3], color[3] + color[4] + color[5]]
	for elem in colorBis:
		if elem > n / 2:
			print("IMPOSSIBLE")
			return
	paddle = ""
	tmp = color.index(max(color))
	paddle += colorList[tmp]
	color[tmp] -= 1
	n -= 1
	while n > 0:
		m = min(color)
		idx = -1
		for i in range(0, 6):
			if color[i] >= m and color[i] > 0:
				if (canBe(colorList.index(paddle[-1]), i)):
					m = color[i]
					idx = i
		if idx == -1:
			print("IMPOSSIBLE")
			return
		paddle += colorList[idx]
		color[idx] -= 1
		n -= 1
	while not canBe(colorList.index(paddle[0]), colorList.index(paddle[-1])):
		l = colorList.index(paddle[-1])
		paddle = paddle[:-1]
		i = len(paddle) - 1
		while i > 0:
			if canBe(colorList.index(paddle[i]), l) and canBe(colorList.index(paddle[i - 1]), l):
				paddle = paddle[0:i] + colorList[l] + paddle[i:]
				break
			i -=1
		if (i == 0):
			print "IMPOSSIBLE"
			return
	print paddle


nbTest = int(raw_input())
for i in range(1, nbTest + 1):
	print "Case #"+ str(i) + ":",
	_main()