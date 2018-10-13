def main():
	scanner = open('D-large.in','r')
	writer = open('D-large.out','w')
	T = int(scanner.readline())
	x = 1
	while x <= T and x <= 50:
		blocks = int(scanner.readline())
		y = 0
		z = 0
		log1 = []
		log2 = []
		line1 = scanner.readline().split()
		i = 0
		j = 0
		while i < len(line1):
			log1.append(float(line1[i]))
			i += 1
			j += 1
			if j < blocks and i == len(line1):
				line1 = scanner.readline().split()
				i = 0
		log1.sort()
		
		line2 = scanner.readline().split()
		i = 0
		j = 0
		while i < len(line2):
			log2.append(float(line2[i]))
			i += 1
			j += 1
			if j < blocks and i == len(line2):
				line2 = scanner.readline().split()
				i = 0
		log2.sort()
		
		logCpy1 = log1.copy()
		logCpy2 = log2.copy()
		while len(logCpy1) > 0:
			Nao = logCpy1[0]
			Ken1 = logCpy2[0]
			if Nao < Ken1:
				logCpy1.pop(0)
				logCpy2.pop(len(logCpy2) - 1)
			elif Nao > Ken1:
				logCpy1.pop(0)
				logCpy2.pop(0)
				y += 1
		
		i = 0
		while i < blocks:
			Nao = log1[i]
			j = 0
			while j < len(log2):
				if Nao < log2[j]:
					log2.pop(j)
					break
				j += 1
			i += 1
		z = len(log2)
		writer.write('Case #%d: %d %d' % (x,y,z))
		if x < T and x < 50:
			writer.write('\n')
		x += 1

if __name__ == '__main__':
	main()