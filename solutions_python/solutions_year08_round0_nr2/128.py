def find_next_train(time, l):
	idx = 0

	if len(l) == 0:
		return -1

	while idx < len(l) and l[idx][0] < time+turna:
		idx = idx + 1

	if len(l) == idx:
		return -1

	return l.pop(idx)[1]

def cmpfunc(x,y):
	return x[0]-y[0]

def time2min(s):
	tm = s.split(':')
	return int(tm[0])*60 + int(tm[1])

def toMinTable(f, loop, ln):
	for x in range(loop):
		sch = f.readline().split(' ')
		ln.append((time2min(sch[0]), time2min(sch[1])))

def find_chain(firstl, secondl):
	flag = 0
	arvtime = firstl.pop(0)[1]

	while arvtime != -1:
		if flag == 0:
			arvtime = find_next_train(arvtime, secondl)
			flag = 1
		else:
			arvtime = find_next_train(arvtime, firstl)
			flag = 0

def mainloop(f):
	atob = []
	btoa = []
	at = bt = 0

	att, btt = f.readline().split(' ')

	if att == 0 or btt == 0:
		return (0,0)

	toMinTable(f, int(att), atob)
	toMinTable(f, int(btt), btoa)

	atob.sort(cmpfunc)
	btoa.sort(cmpfunc)

	while atob != [] and btoa != []:
		if btoa[0][0] < atob[0][0]:
			bt = bt + 1
			find_chain(btoa, atob)
		else:
			at = at + 1
			find_chain(atob, btoa)

	if atob == []:
		bt = bt + len(btoa)
	else:
		at = at + len(atob)
			
	return (at,bt)

f = open('B-large.in','r')

num = int(f.readline())

for x in range(num):
	turna = int(f.readline())
	answer = mainloop(f)
	print 'Case #'+str(x+1)+':', answer[0],answer[1]

f.close()
