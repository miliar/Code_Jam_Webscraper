fin = open('input.in','r')
fout = open('output.out','w')

lines = [line[:-1] for line in fin]

T, l = int(lines[0]), 0
for cT in range(1,T + 1):
	l += 1
	line = lines[l].split()
	d, n = int(line[0]), int(line[1])
	maxTime = 0
	for i in range(n):
		l += 1
		line = lines[l].split()
		k, s = int(line[0]), int(line[1])
		maxTime = max(maxTime, (d - k) / s)
	fout.write('Case  #' + str(cT) + ': ' + str(d / maxTime) + '\n')
