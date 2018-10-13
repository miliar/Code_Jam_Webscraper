import os.path

dir = os.path.dirname(__file__)

def go():
	with open(os.path.join(dir, 'A-large-0.in')) as f_in:
		lines = f_in.readlines()
	with open(os.path.join(dir, 'A-large-0.out'), 'w') as f_out:
		numTests = int(lines[0])
		for case, line in enumerate(lines[1:]):
			movements = line.split(' ')[1:]
			whos = []
			wheres = []
			for i, m in enumerate(movements):
				if i % 2 == 0:
					whos.append(m)
				else:
					wheres.append(int(m))
			movements = zip(whos, wheres)
			res = test(movements)
			outline = 'Case #%s: %s' % (case+1, res)
			print outline
			print
			f_out.write(outline + '\n')

def other(r):
	return 'O' if r == 'B' else 'B'

def test(movements):
	pos = {'B':1, 'O':1}
	time = {'B':0, 'O':0}
	for who, where in movements:
		dist = abs(pos[who] - where)
		print who + ':', pos[who], '=>', where, '====>', dist,
		timeaftermove = time[who] + dist
		othertime = time[other(who)]
		prevtime = time[who]
		pos[who] = where
		time[who] = max(timeaftermove, othertime) + 1
		print ' ========> max(%s+%s, %s) + 1 = %s' % (prevtime, dist, othertime, time[who])
	res = max(time.values())
	return res

go()
