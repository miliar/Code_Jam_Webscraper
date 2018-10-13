def backward(line, i):
	if i <= 0:
		return
	if int(line[i]) < line[i - 1]:
		#line[i] = str('9')
		for j in range(i, len(line)):
			line[j] = str('9')
		line[i - 1] = str(int(line[i - 1]) - 1)
		backward(line, i - 1)

ln = int(input())
for case in range(ln):
	line = input()
	line = list(map(int, line))
	last = 0
	for i, num in enumerate(line):
		if int(num) < last:
			backward(line, i)
		last = int(num)
	print('Case #%d: %d' % (case + 1, int(''.join(map(str, line)))))
