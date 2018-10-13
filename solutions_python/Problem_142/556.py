def makeSame(a,b):
    ret = 0
    j = 0
    i = 0
    while i < len(a):
	if j == len(b):
	    if b[j-1] == a[i]:
		j -= 1
		ret += 1
	    else:
		return -1
	elif b[j] == a[i]:
	    j += 1
	    i += 1
	elif b[j-1] == a[i]:
	    ret += 1
	    i += 1
	elif b[j] == a[i-1]:
	    ret += 1
	    j += 1
	else:
	    return -1
    while j < len(b):
	if b[j] != a[-1]:
	    return -1
	else:
	    j += 1
	    ret += 1
    return ret


f = open('input.in')
fw = open('output.out', 'w')
g = f.readline()
g = f.readline()
case = 1
while g != "":
    arr = []
    for i in range(int(g.replace('\n', ''))):
	arr.append(f.readline().replace('\n', ''))
    m = makeSame(arr[0], arr[1])
    s = ''
    if m == -1:
	s = 'Fegla Won'
    else:
	s = str(m)
    print 'Case #' + str(case) + ': ' + s + '\n',
    fw.write('Case #' + str(case) + ': ' + s + '\n')
    case += 1
    g = f.readline()
