def processEachCase(t_index):
	line = raw_input().strip().split(' ')
	n = int(line[0])
	k = int(line[1])
	if ((k + 1) % (2 ** n)) == 0:
		print "Case #%d: ON" % t_index
	else:
		print "Case #%d: OFF" % t_index
		

t = int(raw_input().strip())
t_index = 1
while t_index <= t:
	processEachCase(t_index)
	t_index = t_index + 1

