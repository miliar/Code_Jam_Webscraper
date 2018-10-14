f = open('1.in', 'r')
o = open('1.out', 'w')

T = int(f.readline().strip())

for t in xrange(T):
    row1 = int(f.readline().strip())
    for i in xrange(4):
	    l1 = f.readline().strip()
	    if i == (row1 - 1):
		    l11 = l1

    row2 = int(f.readline().strip())
    for i in xrange(4):
	    l2 = f.readline().strip()
	    if i == (row2 - 1):
		    l22 = l2
    

    m1 = map(int, l11.strip().split(' '))
    m2 = map(int, l22.strip().split(' '))
    c = 0
    for x in m1:
	    if x in m2:
		    hit = x
		    c = c + 1
    if (c == 1):
	    res = str(hit)
    elif (c > 1):
	    res = "Bad magician!"
    else:
	    res = "Volunteer cheated!"
    s = "Case #%d: %s\n" % (t+1, res)
    o.write(s)
