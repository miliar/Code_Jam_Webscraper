import sys, os

f = open(sys.argv[1],'r')
T = int(f.readline())

for t in range(T):
	tokens = f.readline().split()
	N = int(tokens[0])
	p = {}
	time = {}
	p['O'] = 1
	p['B'] = 1
	time['O'] = 0
	time['B'] = 0
	last_move = 'O'
	for n in range(N):
		who = tokens[n*2 + 1]
		p_to = int(tokens[n*2 + 2])
		dt = abs(p_to - p[who]) + 1
		p[who] = p_to
		if dt + time[who] > time[last_move]:
			time[who] += dt
		else:
			time[who] = time[last_move] + 1
		last_move = who
	print 'Case #%d: %d' %((t+1), time[who])

