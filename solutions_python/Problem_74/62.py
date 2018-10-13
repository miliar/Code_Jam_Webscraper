def xx(words, op, otime, btime, time, color):
	tmp = abs(int(words[2*j+1]) - op) + 1
	op = int(words[2*j+1])
	if otime>=0 and btime==0:
		otime += tmp
		time += tmp
	elif btime>=0 and otime==0:
		if tmp <= btime:
			otime = 1
		else:
			otime = tmp - btime
		time += otime
		btime = 0
	# print '%s %d %d %d %d %d' % (color, tmp, op, otime, btime, time)
	return op, otime, btime, time
	
	
fin = open('in.txt', 'r')
fout = open('out.txt', 'w')
line = fin.readline().strip()
count = int(line)
for i in range(count):
	op = 1
	bp = 1
	otime = 0
	btime = 0
	time = 0
	line = fin.readline().strip()
	line = line[line.index(' ')+1:]
	words = line.split(' ')
	for j in range(len(words)/2):
		if words[2*j] == 'O':
			op, otime, btime, time = xx(words, op, otime, btime, time, 'O')
		elif words[2*j] == 'B':
			bp, btime, otime, time = xx(words, bp, btime, otime, time, 'B')
	fout.write( 'Case #%d: %d\n' % (i+1, time))
			
