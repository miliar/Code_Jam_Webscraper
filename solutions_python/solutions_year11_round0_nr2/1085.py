import sys

f = open(sys.argv[1], 'r')
lines = f.readlines()
lines.pop(0)
f.close()

f = open('asdf.txt', 'w')
c = 0

def format(list):
	return str(list).replace("'", '')

for l in lines:
	c+=1
	l = l.split()
	opposed = 0
	form = 0
	if l[0] == '0':
		next = 1
	elif l[0] == '1':
		form = list(l[1][:2])
		new = l[1][2]
		next = 2
	if l[next] == '0':
		next += 2
	elif l[next] == '1':
		opposed = list(l[next+1][:2])
		next += 3
	
	evoke = []
	for e in l[next]:
		evoke.append(e)
		if form and len(evoke) >= 2 and (evoke[-2:] == [form[0], form[1]] or evoke[-2:] == [form[1], form[0]]):
			evoke.pop()
			evoke.pop()
			evoke.append(new)
		elif opposed and opposed[0] in evoke and opposed[1] in evoke:
			evoke = []
	
	f.write('Case #' + str(c) + ": " + format(evoke) + "\n")
	
f.close()
		