def main():
	scanner = open('B-large.in','r')
	writer = open('B-large.out','w')
	T = int(scanner.readline())
	x = 1
	while x <= T and x <= 100:
		line = scanner.readline().split()
		C = float(line[0])
		F = float(line[1])
		X = float(line[2])
		cps = 2
		totalTime = X / cps
		waitTime = 0
		buyTime = 0
		tempTime = 0
		while totalTime >= tempTime:
			buyTime = C / cps
			waitTime += buyTime
			cps += F
			tempTime = waitTime + (X / cps)
			if tempTime < totalTime:
				totalTime = tempTime
		
		writer.write('Case #%d: %.7f' % (x, round(totalTime, 7)))
		if x < T and x < 100:
			writer.write('\n')
		x += 1

if __name__ == '__main__':
	main()