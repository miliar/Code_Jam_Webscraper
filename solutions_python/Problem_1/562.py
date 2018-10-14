#!/usr/bin/python

f = open('A-large.in', 'r')
o = open('A-large.out', 'w')

tot = eval(f.readline())
cas = 1

def find_far(qt):
	global engine, query
	maxim = -1
	search = query[qt:]

	if engine != '':
		if search.count(engine) == 0:
			return engine

	for u in name:
		if search.count(u) > 0:
			found = search.index(u)

			if found > maxim:
				maxim = found
				new_engine = u
		else:

			new_engine = u
			break
	return new_engine

while cas <= tot:

	s = eval(f.readline())
	sn = 0
	name = []
	while sn < s:
		temp = f.readline()
		name.append(temp[:-1])
		sn = sn + 1

	q = eval(f.readline())
	qn = 0
	if q > 0:
		query = []
		while qn < q:
			temp = f.readline()
			query.append(temp[:-1])
			qn = qn + 1

		counter = 0
		qt = 0
		engine = new_engine = ''

		for i in query:

			if i == engine or engine == '':
				new_engine = find_far(qt)

				if new_engine != engine:
					if engine != '':
						counter = counter + 1
					engine = new_engine
			qt = qt + 1
	else:
		counter = 0
	o.write('Case #' + `cas` + ': ' + `counter` + '\n')
	print 'Case #' + `cas` + ': ' + `counter`
	cas = cas + 1

f.close()
o.close()
