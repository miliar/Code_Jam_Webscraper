colorChars = ['R', 'O', 'Y', 'G', 'B', 'V']
def CtoChar(c):
	return colorChars[c]

def pairOk(c1, c2):
	if c1 != c2 and ((c1+1)%6) != c2 and ((c1+5)%6) != c2:
		return True
	return False

def nextColor(colors, last, startC):
	#print(colors, last)
	l = sorted(enumerate(colors), key=lambda p: p[1], reverse=True)

	for i in range(len(colors)):
		(color, v) = l[i]
		if v == 0:
			return -1
		if i < len(colors) - 1:
			(colorN, vN) = l[i+1]
			if vN == v and pairOk(colorN, last):
				if colorN == startC:
					return colorN
		if i < len(colors) - 2:
			(colorN, vN) = l[i+2]
			if vN == v and pairOk(colorN, last):
				if colorN == startC:
					return colorN
		#print(color, v)
		if pairOk(color, last):
			return color
	return -1


T = int(input())
case = 1

while T>0:
	T -= 1
	[N, R, O, Y, G, B, V] = [int(x) for x in raw_input().strip().split(' ')]

	Colors = [R, O, Y, G, B, V]
	ColorsOrig = Colors
	resultC = []
	result = ''
	last = -1
	while sum(Colors) > 0:
		c = nextColor(Colors, last, -1 if len(resultC)==0 else resultC[0])
		if c == -1:
			result = 'IMPOSSIBLE'
			break
		else:
			result += CtoChar(c)
			resultC.append(c)
			Colors[c] -= 1
		last = c;
	if not pairOk(resultC[0], resultC[-1]):
		result = 'IMPOSSIBLE'
	#if result[0] == 'I':
	#	if R <= Y + B and Y <= R + B and B <= R + Y:
	#		print("ERROR", R, Y, B)
	print('Case #' + str(case) + ': ' + result)
	case += 1