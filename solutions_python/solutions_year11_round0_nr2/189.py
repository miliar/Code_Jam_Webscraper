def parse_param():
    line = raw_input().split()
    C = int(line.pop(0))
    combine = []
    for i in range(C):
	combine.append(line.pop(0))
    D = int(line.pop(0))
    opposed = []
    for i in range(D):
	opposed.append(line.pop(0))
    line.pop(0)
    element_list = []
    for s in line.pop(0):
	element_list.append(s)
    return combine, opposed, element_list

def get_combine(e1, e2, c):
    for cc in c:
	if e1 == cc[0] and e2 == cc[1]:
	    return cc[-1]
	elif e1 == cc[1] and e2 == cc[0]:
	    return cc[-1]
    return '?'

def get_opposed_list(e, d):
    l = []
    for dd in d:
	if e in dd:
	    l.append(dd.replace(e, '', 1))
    return l

def solve(c, d, n):
    e1 = '?'
    res = []
    opposed_list = []
    for e2 in n:
	combine = get_combine(e1, e2, c)
	if combine != '?':
	    res.pop()
	    res.append(combine)
	    e2 = combine
	    l = get_opposed_list(e1, d)
	    if len(l) > 0:
		opposed_list = opposed_list[:-1 * len(l)]
	elif e2 in opposed_list:
	    res = []
	    opposed_list = []
	    e2 = '?'
	else:
	    opposed_list.extend(get_opposed_list(e2, d))
	    res.append(e2)
	e1 = e2
    return res

def make_output(l):
    s = '['
    for j in l[:-1]:
	s += j
	s += ', '
    if len(l) > 0:
	s += l[-1]
    s += ']'
    return s

def main():
    T = int(raw_input())
    for i in range(1, T + 1):
	print "Case #%d:" % i,
	c, d, n = parse_param()
	l = solve(c, d, n)
	print make_output(l)

main()

