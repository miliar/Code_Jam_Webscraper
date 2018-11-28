def h(a):
	if a == 'y':
		return 'a'
	elif a == 'n':
		return 'b'
	elif a == 'f':
		return 'c'
	elif a == 'i':
		return 'd'
	elif a == 'c':
		return 'e'
	elif a == 'w':
		return 'f'
	elif a == 'l':
		return 'g'
	elif a == 'b':
		return 'h'
	elif a == 'k':
		return 'i'
	elif a == 'u':
		return 'j'
	elif a == 'o':
		return 'k'
	elif a == 'm':
		return 'l'
	elif a == 'x':
		return 'm'
	elif a == 's':
		return 'n'
	elif a == 'e':
		return 'o'
	elif a == 'v':
		return 'p'
	elif a == 'z':
		return 'q'
	elif a == 'p':
		return 'r'
	elif a == 'd':
		return 's'
	elif a == 'r':
		return 't'
	elif a == 'j':
		return 'u'
	elif a == 'g':
		return 'v'
	elif a == 't':
		return 'w'
	elif a == 'h':
		return 'x'
	elif a == 'a':
		return 'y'
	elif a == 'q':
		return 'z'
	elif a == ' ':
		return ' '
	elif a == '\n':
		return '\n'
assa = []
a = ""
f = open('A-small-attempt3.in', 'r')
x = f.readline()
p = 1
for y in range((int)(x)):
	ass = f.readline()
	assa.append("Case #"+str(p)+": ")
	for l in range(len(ass)):
		assa.append(h(ass[l]))
	p = p + 1
f.close()		
f = open('jamOut', 'w')
f.write(a.join(assa))
f.close()
