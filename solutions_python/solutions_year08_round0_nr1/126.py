def makelist(f, listname):
	n = f.readline()

	for x in range(int(n)):
		listname.append(f.readline().strip())

def mainloop(f, case):
	engine = []
	query = []
	switch = 0
	cursor = 0

	makelist(f, engine)
	makelist(f, query)

	engine_copy = engine[:]

	while cursor < len(query):
		if engine_copy.count(query[cursor]) != 0 and len(engine_copy) == 1:
			switch = switch + 1
			engine_copy = engine[:]

		try:
			engine_copy.remove(query[cursor])
		except ValueError:
			pass

		cursor = cursor + 1

	return switch

f = open('A-large.in','r')

s = f.readline()

num = int(s)

for x in range(num):
	print 'Case #'+str(x+1)+':', mainloop(f, x+1)

f.close()
