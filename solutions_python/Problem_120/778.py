a = open('small.in')
b = open('result1.in','w')
def area(r,t):
	m = 0
	while True:
		area = int((r+1)**2 - r**2)
		t -= area
		if t < 0:
			return m
		else:
			m += 1
			r += 2


list = []
case = 1
n = 1
for i in a:
    i = i.strip()
    i = i.split(' ')
    if n > 1:
        list = []
        for x in i:
            list.append(int(x))
        r = int(list[0])
        t = int(list[1])
        line = 'Case #%d: '%(case) +str((area(r,t))) + '\n'
        b.write(line)
        case += 1
    n += 1

